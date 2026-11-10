# Environment Keys MCP packages

Downloadable MCP tool/request note packages for the [Environment Keys](https://github.com/EmanuellCarvalhoPires/obsidian-environment-variables) Obsidian plugin.

Each package under `packages/` is a set of `#mcp/tool` and `#api/request` notes for one API (e.g. Jira, Bitbucket, Confluence). The plugin's "Download MCP" screen reads `manifest.json` to list the available packages, and each package's own `manifest.json` to download it whole or one tool at a time.

None of these notes hold credentials: values (URLs, tokens) are filled in at call time from the service notes already in your vault, exactly like any other vault tool.

## Layout

- `manifest.json` — the catalog: id, name, tag and logo of every package, plus (when the package's tools pick an instance through a `service_tag`) the `serviceTag` and the path of that service's `serviceTemplate` note.
- `packages/<id>/manifest.json` — every file in the package, tagged `index`, `tool` or `request`. Each `tool` entry names its paired `request` file.
- `packages/<id>/**/*.md` — the notes themselves, ready to be copied into a vault as-is.
- `scripts/specs.json` — for every package, the URL of the official Atlassian OpenAPI document and how its requests are built (base URL, service placeholders). `csm` has no public spec and is maintained by hand.
- `scripts/sync_specs.py` — compares each package with its official spec and regenerates what changed (standard library only).
- `templates/*.md` — one service-note template per `serviceTag` (e.g. `atlassian-instance.md` for `atlassian/instance`), shared by every package that uses it. The plugin downloads it once, into an "Instances" folder, the first time a package needs that service and none exists yet in the vault.

## Keeping the packages up to date

Atlassian publishes its REST APIs as OpenAPI documents. `scripts/sync_specs.py` downloads them and compares them with every `packages/<id>/mcp.db`:

```bash
python scripts/sync_specs.py --check            # report only; exit 10 when something differs
python scripts/sync_specs.py --apply --prune    # regenerate the databases, index notes and manifests
```

- New operations get a request (and a tool, in packages that have tools) built the same way as the existing ones; deprecated operations are skipped. Experimental ones are tagged `api/stability/experimental`.
- Existing operations whose path or query parameters changed are regenerated in place (same ids and titles).
- Operations that left the spec are deleted with `--prune`; operations the spec now marks as deprecated are only reported.
- Each package records `spec_url`, `spec_version`, `spec_fingerprint` and `synced_at` in its `mcp_package` row, and the catalog `manifest.json` carries `version`, `specVersion` and `updatedAt` per package.

The workflow `.github/workflows/sync-specs.yml` runs this every Monday and opens a pull request with the report. For it to open pull requests, enable *Settings > Actions > General > Allow GitHub Actions to create and approve pull requests*.
