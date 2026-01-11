// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import starlightTypeDoc from "starlight-typedoc";
import { globSync } from "glob";

/**
 * Check if TypeScript source files exist in web/src.
 * Returns true if .ts or .tsx files are found.
 * @returns {boolean} Whether TypeScript files exist
 */
function hasTypeScriptFiles() {
    const tsFiles = globSync("../web/src/**/*.{ts,tsx}", {
        cwd: import.meta.dirname,
        ignore: ["**/*.d.ts", "**/env.d.ts"],
    });
    return tsFiles.length > 0;
}

/**
 * Get Starlight plugins based on available source files.
 * Only includes TypeDoc plugin if TypeScript files exist.
 */
function getPlugins() {
    /** @type {any[]} */
    const plugins = [];

    if (hasTypeScriptFiles()) {
        plugins.push(
            starlightTypeDoc({
                entryPoints: ["../web/src/**/*.ts", "../web/src/**/*.tsx"],
                tsconfig: "../web/tsconfig.json",
                output: "api/typescript",
                sidebar: {
                    label: "TypeScript API",
                    collapsed: true,
                },
            }),
        );
    }

    return plugins;
}

// https://astro.build/config
export default defineConfig({
    site: "https://unidash-linux.github.io",
    base: "/UniDash",
    integrations: [
        starlight({
            title: "UniDash",
            description:
                "Documentation for UniDash - Unified Dashboard for Self-Hosted Applications",
            plugins: getPlugins(),
            social: [
                {
                    icon: "github",
                    label: "GitHub",
                    href: "https://github.com/UniDash-Linux/UniDash",
                },
            ],
            sidebar: [
                {
                    label: "Getting Started",
                    items: [
                        {
                            label: "Introduction",
                            slug: "getting-started/introduction",
                        },
                        {
                            label: "Installation",
                            slug: "getting-started/installation",
                        },
                    ],
                },
                {
                    label: "Architecture",
                    autogenerate: { directory: "architecture" },
                },
                {
                    label: "API Reference",
                    autogenerate: { directory: "api" },
                },
                {
                    label: "Deployment",
                    autogenerate: { directory: "deployment" },
                },
                {
                    label: "Development",
                    autogenerate: { directory: "development" },
                },
                {
                    label: "Community",
                    items: [
                        {
                            label: "Contributing",
                            link: "https://github.com/UniDash-Linux/UniDash/blob/main/CONTRIBUTING.md",
                        },
                        {
                            label: "Code of Conduct",
                            link: "https://github.com/UniDash-Linux/UniDash/blob/main/CODE_OF_CONDUCT.md",
                        },
                    ],
                },
            ],
        }),
    ],
});
