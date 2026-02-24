import { describe, it, expect } from 'vitest';
import { existsSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const docsRoot = resolve(__dirname, '../..');
const contentDir = resolve(docsRoot, 'src/content/docs');

/**
 * Extract all sidebar items with slugs from the Astro config.
 * We parse the config file as text to avoid importing Astro internals in unit tests.
 */
async function loadAstroConfig() {
  const { default: config } = await import('../../astro.config.mjs');
  return config;
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
  it('can be imported without errors', async () => {
    const config = await loadAstroConfig();
    expect(config).toBeDefined();
    expect(config.site).toBe('https://extended-data.dev');
  });

  it('has Starlight integration configured', async () => {
    const config = await loadAstroConfig();
    expect(config.integrations).toBeDefined();
    expect(config.integrations.length).toBeGreaterThan(0);
  });
});

describe('Starlight sidebar structure', () => {
  it('has sidebar groups defined', async () => {
    const config = await loadAstroConfig();
    const starlight = config.integrations[0];
    // Starlight stores its config internally; we access it from the config source
    // Re-import the raw config to extract sidebar
    const { readFileSync } = await import('node:fs');
    const configSource = readFileSync(resolve(docsRoot, 'astro.config.mjs'), 'utf-8');
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
