import { describe, it, expect } from "vitest";
import { existsSync, readFileSync } from "fs";
import { resolve } from "path";

const projectRoot = resolve(__dirname, "..");

describe("Frontend Setup Validation", () => {
  it("should have TypeScript configured with strict mode", () => {
    const tsconfigPath = resolve(projectRoot, "tsconfig.json");
    expect(existsSync(tsconfigPath)).toBe(true);

    const tsconfig = JSON.parse(readFileSync(tsconfigPath, "utf-8"));
    expect(tsconfig.extends).toContain("strict");
  });

  it("should have Tailwind installed", () => {
    const packagePath = resolve(projectRoot, "package.json");
    const packageJson = JSON.parse(readFileSync(packagePath, "utf-8"));

    expect(packageJson.dependencies).toHaveProperty("tailwindcss");
  });

  it("should have React installed", () => {
    const packagePath = resolve(projectRoot, "package.json");
    const packageJson = JSON.parse(readFileSync(packagePath, "utf-8"));

    expect(packageJson.dependencies).toHaveProperty("react");
    expect(packageJson.dependencies).toHaveProperty("react-dom");
  });

  it("should have Nanostores installed", () => {
    const packagePath = resolve(projectRoot, "package.json");
    const packageJson = JSON.parse(readFileSync(packagePath, "utf-8"));

    expect(packageJson.dependencies).toHaveProperty("nanostores");
    expect(packageJson.dependencies).toHaveProperty("@nanostores/react");
  });

  it("should have ESLint configured", () => {
    const eslintConfigPath = resolve(projectRoot, "eslint.config.js");
    expect(existsSync(eslintConfigPath)).toBe(true);
  });

  it("should have Prettier configured", () => {
    const prettierConfigPath = resolve(projectRoot, ".prettierrc");
    expect(existsSync(prettierConfigPath)).toBe(true);
  });
});
