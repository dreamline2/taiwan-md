"""link-target — verify markdown link path is well-formed and resolves.

Two-phase validation of internal markdown links `[text](/path/)`:

  Phase 1 — CASING: `/en/History/...` is broken because Astro routes lowercase
            the category segment (CATEGORY_MAPPING in `[category]/[slug].astro`
            uses lowercase keys). Auto-fixable.

  Phase 2 — EXISTENCE: `/en/history/non-existent-slug/` is broken even with
            correct casing. Cross-checks against the actual filesystem
            (`knowledge/{lang}/{Category}/{slug}.md`). Not auto-fixable
            (which slug did the author mean? human must decide).

Source-layer counterpart of `verify-internal-links.sh` (post-build dist scan).
Catching at source means pre-commit / pre-PR gates fire instead of waiting
for the full build.

Trigger: 2026-05-04 jovial-feistel session — CI run 25325225046 failed with
649 broken `](/lang/UpperCase/...)` links (Phase 1). Cheyu pushed for Phase 2
during fix: "目前有檢查內容交叉連結能否到達真實頁面嗎？沒有的話怎麼改良工具".
"""

from __future__ import annotations
import re
from pathlib import Path
from typing import Any, Iterator

from ..types import FileTarget, Severity, Violation


CHECK_NAME = "link-target"
DIMENSION = "structure"
# Phase 1 (casing) is HARD inside check(); Phase 2 (existence) is WARN by
# default so pre-commit doesn't block parallel cron / agent work that touches
# articles with long-accumulated broken slugs. release-pr profile sets
# fail_on="warn" so CI still catches existence issues.
DEFAULT_SEVERITY = Severity.HARD
EDITORIAL_REF = "src/pages/{lang}/[category]/[slug].astro CATEGORY_MAPPING (lowercase routing) + knowledge/{lang}/{Category}/*.md (existence)"
APPLIES_TO = ["*"]

_LANGS = {"en", "ja", "ko", "fr", "es", "zh-TW"}
_TRANSLATION_LANGS = {"en", "ja", "ko", "fr", "es"}
_KNOWLEDGE_ROOT = Path("knowledge")

# Phase 1: capitalized category in link path.
_RE_CASING = re.compile(
    rf"(\]\(/(?:{'|'.join(sorted(_LANGS))})/)([A-Z][a-zA-Z-]*)(/[^)]*\))"
)

# Phase 2: any internal absolute link, for existence check.
# Captures the path part (without anchor/query) for lookup.
_RE_INTERNAL = re.compile(r"\]\((/[^)\s#?]+)(?:[#?][^)]*)?\)")


def _existing_link_targets() -> set[str]:
    """Set of valid internal link paths (no trailing slash, no anchor).

    Format:
      `/{lang}/{category-lower}/{slug}` for translations
      `/{category-lower}/{slug}`        for zh-TW (default routing)
      `/zh-TW/{category-lower}/{slug}`  for explicit zh-TW prefix

    Cached per-process — call `_reset_cache()` in tests when filesystem changes.
    """
    cached = getattr(_existing_link_targets, "_cache", None)
    if cached is not None:
        return cached
    paths: set[str] = set()
    if _KNOWLEDGE_ROOT.exists():
        for entry in _KNOWLEDGE_ROOT.iterdir():
            if not entry.is_dir() or entry.name.startswith("_"):
                continue
            if entry.name in _TRANSLATION_LANGS:
                lang = entry.name
                for cat_dir in entry.iterdir():
                    if not cat_dir.is_dir() or cat_dir.name.startswith("_"):
                        continue
                    cat_lower = cat_dir.name.lower()
                    for md in cat_dir.glob("*.md"):
                        if md.name.startswith("_"):
                            continue
                        paths.add(f"/{lang}/{cat_lower}/{md.stem}")
            else:
                # zh-TW category dir at root.
                cat_lower = entry.name.lower()
                for md in entry.glob("*.md"):
                    if md.name.startswith("_"):
                        continue
                    paths.add(f"/{cat_lower}/{md.stem}")
                    paths.add(f"/zh-TW/{cat_lower}/{md.stem}")
    _existing_link_targets._cache = paths  # type: ignore[attr-defined]
    return paths


def _reset_cache() -> None:
    """Test helper — invalidate the path cache."""
    if hasattr(_existing_link_targets, "_cache"):
        delattr(_existing_link_targets, "_cache")


def _line_col(text: str, pos: int) -> tuple[int, int]:
    line = text.count("\n", 0, pos) + 1
    line_start = text.rfind("\n", 0, pos) + 1
    col = pos - line_start + 1
    return line, col


def _snippet(body: str, pos: int, end: int) -> str:
    line_start = body.rfind("\n", 0, pos) + 1
    line_end = body.find("\n", end)
    if line_end == -1:
        line_end = len(body)
    return body[line_start:line_end].strip()[:120]


def _looks_like_article_path(path: str) -> bool:
    """Path matches `/lang/cat/slug` or `/cat/slug` shape — worth resolving.

    Skips `/about/`, `/dashboard/`, `/contribute/`, etc. (static pages handled
    by other gates) and weird shapes like `/api/...`.
    """
    parts = path.strip("/").split("/")
    if len(parts) == 3 and parts[0] in _LANGS:
        return True
    if len(parts) == 2 and parts[0] not in _LANGS and parts[0] not in {
        "api", "og-images", "assets", "_astro",
    }:
        return True
    return False


def check(target: FileTarget, config: dict[str, Any]) -> Iterator[Violation]:
    body = target.body
    valid = _existing_link_targets()

    # Phase 1: casing violations — HARD (auto-fixable, obvious)
    casing_positions: set[int] = set()
    for m in _RE_CASING.finditer(body):
        casing_positions.add(m.start())
        category = m.group(2)
        line, col = _line_col(body, m.start())
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.HARD,
            message=f"link 路徑 category 必須小寫：/{category}/ → /{category.lower()}/",
            line=line,
            col=col,
            snippet=_snippet(body, m.start(), m.end()),
            fix_suggestion=f"{m.group(1)}{category.lower()}{m.group(3)}",
            editorial_ref=EDITORIAL_REF,
        )

    # Phase 2: existence violations — WARN (not auto-fixable, judgment call)
    for m in _RE_INTERNAL.finditer(body):
        if m.start() in casing_positions:
            continue  # already flagged by Phase 1; skip until casing is fixed
        path = m.group(1).rstrip("/")
        if not _looks_like_article_path(path):
            continue
        # Canonicalize: lowercase the category segment for lookup
        # (after Phase 1 fix all categories will be lowercase, but be defensive).
        parts = path.strip("/").split("/")
        if parts[0] in _LANGS:
            # /lang/cat/slug
            parts[1] = parts[1].lower()
        else:
            # /cat/slug
            parts[0] = parts[0].lower()
        canonical = "/" + "/".join(parts)
        if canonical in valid:
            continue
        line, col = _line_col(body, m.start())
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=f"link 目標不存在：{path}",
            line=line,
            col=col,
            snippet=_snippet(body, m.start(), m.end()),
            fix_suggestion=None,  # human decides which slug
            editorial_ref=EDITORIAL_REF,
        )


def fix(target: FileTarget, config: dict[str, Any]) -> bool:
    """Phase 1 only: lowercase the category segment of every matching link.

    Operates on `target.text` directly (full file). Safe because the regex
    only matches markdown link syntax `](/lang/Cap/...)` which won't appear
    inside YAML frontmatter as a real link target. Avoids the body-vs-text
    splice trap (loader pads body with leading newlines for line-number
    alignment, which breaks naive `text.rfind(body)`).

    Phase 2 (existence) is NOT auto-fixed — the slug ambiguity needs a human.

    Returns True if file was modified.
    """
    new_text = _RE_CASING.sub(
        lambda m: f"{m.group(1)}{m.group(2).lower()}{m.group(3)}",
        target.text,
    )
    if new_text == target.text:
        return False
    target.path.write_text(new_text, encoding="utf-8")
    return True
