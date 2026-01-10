// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

// https://astro.build/config
export default defineConfig({
    site: "https://unidash-linux.github.io",
    base: "/UniDash",
    integrations: [
        starlight({
            title: "UniDash",
            description:
                "Documentation for UniDash - Unified Dashboard for Self-Hosted Applications",
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
            ],
        }),
    ],
});
