#!/usr/bin/env node
/**
 * Script to generate screenshots of UniDash mockups.
 * Captures each view in both light and dark modes.
 */

import puppeteer from 'puppeteer';
import { mkdir } from 'fs/promises';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { execSync } from 'child_process';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = join(__dirname, '..');
const HTML_FILE = join(PROJECT_ROOT, '_bmad-output/planning-artifacts/ux-design-directions.html');
const OUTPUT_DIR = join(PROJECT_ROOT, 'docs/src/assets/screenshots');

// Views to capture with their selector and description
const VIEWS = [
  { id: 'standard', name: 'desktop-standard', desc: 'Bureau Desktop - Standard', selector: '.desktop-frame' },
  { id: 'compact', name: 'desktop-compact', desc: 'Bureau Desktop - Compact', selector: '.desktop-frame' },
  { id: 'minimal', name: 'desktop-minimal', desc: 'Bureau Desktop - Minimal', selector: '.desktop-frame' },
  { id: 'store', name: 'store', desc: 'App Store', selector: '.desktop-frame' },
  { id: 'wizard', name: 'wizard', desc: 'Installation Wizard', selector: '.desktop-frame' },
  { id: 'desktop', name: 'desktop-icons', desc: 'Bureau avec icônes', selector: '.desktop-frame' },
  { id: 'tiling-2col', name: 'tiling-2col', desc: 'Tiling 2 colonnes', selector: '.desktop-frame' },
  { id: 'tiling-quad', name: 'tiling-quad', desc: 'Tiling 4 quadrants', selector: '.desktop-frame' },
  { id: 'mobile', name: 'mobile', desc: 'Vue Mobile', selector: '.mobile-frame' },
  { id: 'mobile-desktop', name: 'mobile-desktop', desc: 'Bureau Mobile', selector: '.mobile-frame' },
  { id: 'app-drawer', name: 'app-drawer-desktop', desc: 'Tiroir Apps Desktop', selector: '.desktop-frame' },
  { id: 'app-drawer-mobile', name: 'app-drawer-mobile', desc: 'Tiroir Apps Mobile', selector: '.mobile-frame' },
];

async function captureScreenshots() {
  await mkdir(OUTPUT_DIR, { recursive: true });

  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1200 });

  await page.goto(`file://${HTML_FILE}`, { waitUntil: 'networkidle0' });

  // Remove border-radius from frames for clean screenshots
  await page.addStyleTag({
    content: `
      .desktop-frame, .mobile-frame {
        border-radius: 0 !important;
      }
    `
  });

  for (const view of VIEWS) {
    for (const theme of ['light', 'dark']) {
      // Set theme
      if (theme === 'dark') {
        await page.evaluate(() => {
          document.querySelector('html').classList.add('dark');
        });
      } else {
        await page.evaluate(() => {
          document.querySelector('html').classList.remove('dark');
        });
      }

      // Navigate to view by directly manipulating DOM (avoiding event.target issue)
      await page.evaluate((viewId) => {
        // Hide all mockups
        document.querySelectorAll('.mockup-container').forEach(el => {
          el.classList.remove('active');
        });
        // Show selected mockup
        const target = document.getElementById(viewId);
        if (target) {
          target.classList.add('active');
        }
      }, view.id);

      // Wait for transition
      await new Promise(resolve => setTimeout(resolve, 300));

      // Find the frame element
      const frameSelector = `#${view.id} ${view.selector}`;
      const frame = await page.$(frameSelector);

      if (frame) {
        const filename = `${view.name}-${theme}.png`;
        const filepath = join(OUTPUT_DIR, filename);

        await frame.screenshot({ path: filepath });
        console.log(`✓ ${filename} - ${view.desc} (${theme})`);
      } else {
        console.log(`✗ Could not find ${frameSelector}`);
      }
    }
  }

  await browser.close();
  console.log(`\nScreenshots saved to: ${OUTPUT_DIR}`);

  // Compress PNGs with pngquant if available
  try {
    execSync(`pngquant --force --quality=65-80 --ext .png ${OUTPUT_DIR}/*.png`, { stdio: 'inherit' });
    console.log('Screenshots compressed with pngquant');
  } catch {
    console.log('pngquant not available, skipping compression');
  }
}

captureScreenshots().catch(console.error);
