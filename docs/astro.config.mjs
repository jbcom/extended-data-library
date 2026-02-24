// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
  site: 'https://extended-data.dev',
  integrations: [
    starlight({
      title: 'Extended Data',
      tagline: 'Production Python Infrastructure',
      customCss: ['./src/styles/custom.css'],
      logo: {
        light: './src/assets/logo-dark.svg',
        dark: './src/assets/logo.svg',
        alt: 'Extended Data',
        replacesTitle: false,
      },
      favicon: '/favicon.svg',
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/jbcom/extended-data-library' },
      ],
      head: [
        {
          tag: 'meta',
          attrs: {
            property: 'og:title',
            content: 'Extended Data - Production Python Infrastructure',
          },
        },
        {
          tag: 'meta',
          attrs: {
            property: 'og:description',
            content: 'Battle-tested Python libraries for serialization, input handling, structured logging, and vendor integrations. Built for production.',
          },
        },
        {
          tag: 'meta',
          attrs: {
            name: 'twitter:card',
            content: 'summary_large_image',
          },
        },
        {
          tag: 'link',
          attrs: {
            rel: 'icon',
            href: '/favicon.svg',
            type: 'image/svg+xml',
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
            { label: 'Overview & API', slug: 'api/vendor-connectors' },
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
          label: 'Ecosystem',
          items: [
            { label: 'jbcom Hub', link: 'https://jbcom.github.io', attrs: { target: '_blank' } },
            { label: 'Agentic (AI)', link: 'https://agentic.dev', attrs: { target: '_blank' } },
            { label: 'Strata (Games)', link: 'https://strata.game', attrs: { target: '_blank' } },
          ],
        },
      ],
      editLink: {
        baseUrl: 'https://github.com/jbcom/extended-data-library/edit/main/docs/',
      },
      lastUpdated: true,
    }),
  ],
});
