// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
  site: 'https://extended-data-library.github.io',
  integrations: [
    starlight({
      title: 'Extended Data',
      tagline: 'Enterprise Python Infrastructure',
      customCss: ['./src/styles/custom.css'],
      logo: {
        src: './src/assets/houston.webp',
        alt: 'Extended Data',
      },
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/extended-data-library' },
      ],
      head: [
        {
          tag: 'meta',
          attrs: {
            property: 'og:title',
            content: 'Extended Data - Enterprise Python Infrastructure',
          },
        },
        {
          tag: 'meta',
          attrs: {
            property: 'og:description',
            content: 'Battle-tested Python utilities for serialization, input handling, logging, and vendor integrations.',
          },
        },
      ],
      sidebar: [
        {
          label: 'Getting Started',
          items: [
            { label: 'Introduction', slug: 'getting-started' },
          ],
        },
        {
          label: 'Extended Data Types',
          items: [
            { label: 'Overview', slug: 'core/data-types' },
            { label: 'API Reference', slug: 'api/extended-data-types', attrs: { class: 'api-link' } },
          ],
        },
        {
          label: 'Lifecycle Logging',
          items: [
            { label: 'Overview', slug: 'packages/logging' },
            { label: 'API Reference', slug: 'api/lifecyclelogging', attrs: { class: 'api-link' } },
          ],
        },
        {
          label: 'Directed Inputs',
          items: [
            { label: 'Overview', slug: 'packages/inputs' },
            { label: 'API Reference', slug: 'api/directed-inputs-class', attrs: { class: 'api-link' } },
          ],
        },
        {
          label: 'Vendor Connectors',
          items: [
            { label: 'Overview', slug: 'api/vendor-connectors' },
            { label: 'API Reference', slug: 'api/vendor-connectors-api', attrs: { class: 'api-link' } },
          ],
        },
        {
          label: 'SecretSync',
          items: [
            { label: 'Overview', slug: 'api/secretsync' },
          ],
        },
        {
          label: 'Packages',
          items: [
            { label: 'Overview', slug: 'packages' },
          ],
        },
        {
          label: 'Enterprise',
          items: [
            { label: 'jbcom Hub', link: 'https://jbcom.github.io', attrs: { target: '_blank' } },
            { label: 'Agentic (AI)', link: 'https://agentic.dev', attrs: { target: '_blank' } },
            { label: 'Strata (Games)', link: 'https://strata.game', attrs: { target: '_blank' } },
          ],
        },
      ],
      editLink: {
        baseUrl: 'https://github.com/extended-data-library/extended-data-types/edit/main/docs/',
      },
      lastUpdated: true,
    }),
  ],
});
