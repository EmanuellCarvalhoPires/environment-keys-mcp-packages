# Environment Keys MCP packages

Downloadable MCP tool/request note packages for the [Environment Keys](https://github.com/EmanuellCarvalhoPires/obsidian-environment-variables) Obsidian plugin.

Each package under `packages/` is a set of `#mcp/tool` and `#api/request` notes for one API (e.g. Jira, Bitbucket, Confluence). The plugin's "Download MCP" screen reads `manifest.json` to list the available packages, and each package's own `manifest.json` to download it whole or one tool at a time.

None of these notes hold credentials: values (URLs, tokens) are filled in at call time from the service notes already in your vault, exactly like any other vault tool.

## Layout

- `manifest.json` — the catalog: id, name, tag and logo of every package.
- `packages/<id>/manifest.json` — every file in the package, tagged `index`, `tool` or `request`. Each `tool` entry names its paired `request` file.
- `packages/<id>/**/*.md` — the notes themselves, ready to be copied into a vault as-is.
