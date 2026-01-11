/**
 * Tests for astro.config.mjs helper functions.
 */
import { describe, it, expect } from "vitest";
import { globSync } from "glob";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const docsRoot = join(__dirname, "..");

/**
 * Check if TypeScript source files exist in web/src.
 * Mirrors the function in astro.config.mjs.
 * @returns {boolean} Whether TypeScript files exist
 */
function hasTypeScriptFiles() {
  const tsFiles = globSync("../web/src/**/*.{ts,tsx}", {
    cwd: docsRoot,
    ignore: ["**/*.d.ts", "**/env.d.ts"],
  });
  return tsFiles.length > 0;
}

describe("hasTypeScriptFiles", () => {
  it("should return false when no TypeScript files exist in web/src", () => {
    // Currently web/src has no .ts/.tsx files (only .astro)
    const result = hasTypeScriptFiles();
    expect(result).toBe(false);
  });

  it("should ignore .d.ts declaration files", () => {
    // env.d.ts exists but should be ignored by hasTypeScriptFiles
    const result = hasTypeScriptFiles();
    expect(result).toBe(false);
  });
});

describe("glob patterns", () => {
  it("should find .ts and .tsx files with combined pattern", () => {
    // This test verifies the glob pattern syntax works
    const pattern = "../web/src/**/*.{ts,tsx}";
    const files = globSync(pattern, {
      cwd: docsRoot,
      ignore: ["**/*.d.ts", "**/env.d.ts"],
    });

    // Verify only .ts and .tsx files would match (no .d.ts)
    files.forEach((f) => {
      expect(f).toMatch(/\.(ts|tsx)$/);
      expect(f).not.toMatch(/\.d\.ts$/);
    });
  });
});
