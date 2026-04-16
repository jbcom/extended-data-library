import { describe, it, expect } from 'vitest';
import { existsSync, readFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const docsRoot = resolve(__dirname, '../..');
const contentDir = resolve(docsRoot, 'src/content/docs');

function loadAstroConfigSource(): string {
  return readFileSync(resolve(docsRoot, 'astro.config.mjs'), 'utf-8');
}

/**
 * Recursively collect all slug references from sidebar items.
 */
function collectSlugs(items: any[]): { label: string; slug: string }[] {
  const slugs: { label: string; slug: string }[] = [];
  for (const item of items) {
    if (item.slug) {
      slugs.push({ label: item.label, slug: item.slug });
    }
    if (item.items) {
      slugs.push(...collectSlugs(item.items));
    }
  }
  return slugs;
}

/**
 * Given a slug, resolve the expected content file path.
 * Astro Starlight maps slugs to files like:
 *   "getting-started" -> src/content/docs/getting-started.md(x)
 *   "packages" -> src/content/docs/packages/index.md(x)
 */
function resolveSlugToFile(slug: string): string | null {
  const extensions = ['.md', '.mdx'];

  // Direct file match: slug.md or slug.mdx
  for (const ext of extensions) {
    const filePath = resolve(contentDir, `${slug}${ext}`);
    if (existsSync(filePath)) return filePath;
  }

  // Index file match: slug/index.md or slug/index.mdx
  for (const ext of extensions) {
    const filePath = resolve(contentDir, slug, `index${ext}`);
    if (existsSync(filePath)) return filePath;
  }

  return null;
}

describe('Astro configuration', () => {
  it('defines the production site URL', () => {
    const configSource = loadAstroConfigSource();
    expect(configSource).toContain("site: 'https://extended-data.dev'");
  });

  it('has Starlight integration configured', () => {
    const configSource = loadAstroConfigSource();
    expect(configSource).toContain("import starlight from '@astrojs/starlight'");
    expect(configSource).toContain('starlight({');
  });
});

describe('Starlight sidebar structure', () => {
  it('has sidebar groups defined', () => {
    const configSource = loadAstroConfigSource();
    expect(configSource).toContain('sidebar');
  });
});

describe('Sidebar slug integrity', () => {
  // Static content slugs from the sidebar config.
  // API Reference entries use `link` (not `slug`) because they point to
  // autodoc2-generated content that only exists after the Sphinx build step.
  // Only `slug`-based entries are validated here.
  const sidebarSlugs = [
    { label: 'Introduction', slug: 'getting-started' },
    { label: 'Overview (Data Types)', slug: 'core/data-types' },
    { label: 'Overview (Logging)', slug: 'packages/logging' },
    { label: 'Overview (Inputs)', slug: 'packages/inputs' },
    { label: 'Overview (SecretSync)', slug: 'api/secretsync' },
    { label: 'Overview (Packages)', slug: 'packages' },
  ];

  for (const { label, slug } of sidebarSlugs) {
    it(`"${label}" (${slug}) maps to an existing content file`, () => {
      const filePath = resolveSlugToFile(slug);
      expect(
        filePath,
        `Sidebar entry "${label}" references slug "${slug}" but no matching content file was found in ${contentDir}. ` +
        `Expected one of: ${slug}.md, ${slug}.mdx, ${slug}/index.md, or ${slug}/index.mdx`
      ).not.toBeNull();
    });
  }
});
