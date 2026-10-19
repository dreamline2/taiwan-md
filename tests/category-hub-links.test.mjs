import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { stripTypeScriptTypes } from 'node:module';
import { test } from 'node:test';
import { ENABLED_LANGUAGE_CODES } from '../src/config/languages.mjs';

// Exercise the actual Astro resolver, not a copy of its URL logic.
// Astro.props prevents importing the whole frontmatter as a Node module.
const source = readFileSync(
  new URL('../src/templates/category-hub.template.astro', import.meta.url),
  'utf8',
);
const prefix = source.match(/^const langUrlPrefix = .*;$/m)?.[0];
const start = source.indexOf('function resolveWikilinks(');
const end = source.indexOf('\nconst resolvedContent =', start);
assert.ok(prefix && start >= 0 && end > start, 'Hub resolver must be present');
const resolve = new Function(
  'lang',
  'articles',
  'md',
  'category',
  stripTypeScriptTypes(`${prefix}\n${source.slice(start, end)}`) +
    '\nreturn resolveWikilinks(md, category);',
);
const articles = [{ title: '야시장 문화', slug: 'night-market-culture' }];

for (const lang of ENABLED_LANGUAGE_CODES) {
  test(`hub article links preserve ${lang} routing`, () => {
    const base = lang === 'zh-TW' ? '' : `/${lang}`;
    const url = `${base}/food/night-market-culture`;
    assert.equal(
      resolve(lang, articles, '**[[야시장 문화]]**', 'food'),
      `<a class="topic-pill" href="${url}"><strong>야시장 문화</strong></a>`,
    );
    assert.equal(
      resolve(lang, articles, '[[night-market-culture|Night markets]]', 'food'),
      `<a class="topic-pill" href="${url}">Night markets</a>`,
    );
    assert.equal(
      resolve(lang, articles, '[[_Culture Hub|Culture]]', 'food'),
      `<a class="topic-pill" href="${base}/culture">Culture</a>`,
    );
  });
}

test('unresolved hub wikilinks remain text, not fabricated routes', () => {
  assert.equal(resolve('ko', articles, '[[Missing]]', 'food'), 'Missing');
  assert.equal(
    resolve('ko', articles, '**[[Missing|Label]]**', 'food'),
    '**Label**',
  );
});
