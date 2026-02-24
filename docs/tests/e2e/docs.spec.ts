import { test, expect } from '@playwright/test';

test.describe('Documentation site', () => {
  test('homepage loads with correct title', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveTitle(/Extended Data/);
  });

  test('homepage has hero content', async ({ page }) => {
    await page.goto('/');
    const hero = page.locator('.hero');
    await expect(hero).toBeVisible();
  });

  test('navigation sidebar is present', async ({ page }) => {
    // Navigate to a docs page (not splash) to get the sidebar
    await page.goto('/getting-started/');
    await page.waitForLoadState('networkidle');
    const sidebar = page.locator('nav[aria-label="Main"]');
    await expect(sidebar).toBeVisible({ timeout: 10_000 });
  });

  test('sidebar contains expected sections', async ({ page }) => {
    await page.goto('/getting-started/');
    const sidebar = page.locator('nav[aria-label="Main"]');
    const sidebarText = await sidebar.textContent();

    const expectedSections = [
      'Getting Started',
      'Extended Data Types',
      'Lifecycle Logging',
      'Directed Inputs',
      'Vendor Connectors',
    ];

    for (const section of expectedSections) {
      expect(sidebarText).toContain(section);
    }
  });
});

test.describe('Page navigation', () => {
  test('Getting Started page loads', async ({ page }) => {
    await page.goto('/getting-started/');
    await expect(page).toHaveTitle(/Introduction|Getting Started/);
    const main = page.locator('main');
    await expect(main).toBeVisible();
  });

  test('API reference page loads', async ({ page }) => {
    await page.goto('/core/data-types/');
    await expect(page).toHaveTitle(/Extended Data Types|Overview/);
    const main = page.locator('main');
    await expect(main).toBeVisible();
  });

  test('navigating from sidebar works', async ({ page }) => {
    await page.goto('/getting-started/');

    // Click on a sidebar link to navigate to another page
    const sidebarLink = page.locator('nav[aria-label="Main"] a[href*="core/data-types"]');
    if (await sidebarLink.count() > 0) {
      await sidebarLink.first().click();
      await expect(page).toHaveURL(/\/core\/data-types\//);
      const main = page.locator('main');
      await expect(main).toBeVisible();
    }
  });
});

test.describe('Error handling', () => {
  test('invalid route returns 404', async ({ page }) => {
    const response = await page.goto('/this-page-does-not-exist/');
    // Astro dev server returns 404 for missing pages
    expect(response?.status()).toBe(404);
  });
});

test.describe('Sidebar link integrity', () => {
  test('all sidebar links resolve without errors', async ({ page }) => {
    await page.goto('/getting-started/');

    // Collect all internal sidebar links (exclude external links)
    const sidebarLinks = page.locator('nav[aria-label="Main"] a[href^="/"]');
    const count = await sidebarLinks.count();
    expect(count).toBeGreaterThan(0);

    const hrefs: string[] = [];
    for (let i = 0; i < count; i++) {
      const href = await sidebarLinks.nth(i).getAttribute('href');
      if (href) hrefs.push(href);
    }

    // Deduplicate
    const uniqueHrefs = [...new Set(hrefs)];

    // Visit each link and verify it does not return a server error
    for (const href of uniqueHrefs) {
      const response = await page.goto(href);
      expect(
        response?.status(),
        `Sidebar link "${href}" returned status ${response?.status()}`
      ).toBeLessThan(500);
    }
  });
});
