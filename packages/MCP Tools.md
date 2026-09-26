---
tags:
  - moc
  - mcp
  - api
up: "[[APIs]]"
---
# MCP Tools

Index of the MCP tools and request notes of the **Environment Keys** plugin. Each tool is a note tagged `#mcp/tool` that points to a request note (`#api/request`). The values of each instance (URL, IDs and token) live only in the service notes.

## How the AI picks a tool

1. **App:** open the app index below or filter by the `api/app/*` tag.
2. **Resource:** filter by the API category with `api/resource/*` (e.g. `api/resource/issues`, `api/resource/issue-comments`).
3. **Operation:** `api/operation/list`, `get`, `search`, `create`, `update`, `delete` or `action`.
4. **Effect:** `api/effect/read` or `api/effect/write`. Write tools have `writes: true` and only run with the user's authorization.
5. **Instance:** every tool receives the `instance` parameter, with the list of the service notes of that service.
6. **Call:** tools marked ⭐ appear directly in the client tool list. The others (`expose: false`) run with `run_vault_tool({ name, arguments })`.

## Service notes (instances)

| Service | Service tag | Instance index |
| --- | --- | --- |
| Atlassian apps (Jira, JSW, JSM, Confluence, Assets, Automation, Forms, CSM, JSM Ops, Admin, SCIM) | `atlassian/instance` | [[Jira Instance Access]] |
| Bitbucket | `bitbucket/workspace` | [[Bitbucket Access]] |
| Trello | `trello/account` | [[Trello Access]] |

Notes tagged `template` are left out of the instance list.

## Apps

| App                              | Index                      | Tools | Requests only | Status                               |
| -------------------------------- | -------------------------- | ----- | ------------- | ------------------------------------ |
| Jira (platform, API v3)          | [[MCP - Jira v3]]          | 552   | 43            | created and tested                   |
| Jira Software (Agile and DevOps) | [[MCP - JSW]]              | 61    | 44            | created and tested                   |
| Jira Service Management          | [[MCP - JSM]]              | 73    | 1             | created and tested                   |
| Confluence (API v2)              | [[MCP - Confluence v2]]    | 218   | 0             | created                              |
| Confluence (API v1)              | [[MCP - Confluence v1]]    | 121   | 9             | created                              |
| JSM Assets                       | [[MCP - Assets]]           | 60    | 1             | created and tested                   |
| Automation                       | [[MCP - Automation]]       | 15    | 0             | created                              |
| Bitbucket                        | [[MCP - Bitbucket]]        | 265   | 3             | created (workspace slug missing)     |
| JSM Ops                          | [[MCP - JSM Ops]]          | 0     | 240           | requests only                        |
| Forms                            | [[MCP - Forms]]            | 0     | 34            | requests only                        |
| Customer Service Management      | [[MCP - CSM]]              | 0     | 60            | requests only                        |
| Admin API Access                 | [[MCP - Admin API Access]] | 0     | 21            | requests only                        |
| Admin Control                    | [[MCP - Admin Control]]    | 0     | 22            | requests only                        |
| Admin DLP                        | [[MCP - Admin DLP]]        | 0     | 8             | requests only                        |
| Admin Organizations              | [[MCP - Admin Orgs]]       | 0     | 45            | requests only                        |
| Admin User Management            | [[MCP - Admin Users]]      | 0     | 10            | requests only                        |
| SCIM (User Provisioning)         | [[MCP - SCIM]]             | 0     | 24            | requests only                        |
| Trello                           | [[MCP - Trello]]           | 0     | 261           | requests only (account note missing) |

## Generic tools

They run any request note by name (`request`) with the values of its placeholders (`parameters`). Use them for the APIs that are requests only.

| Tool | Service | Writes data |
| --- | --- | --- |
| [[atlassian_request_read]] | Atlassian (`atlassian/instance`) | no (GET/HEAD only) |
| [[atlassian_request_write]] | Atlassian | yes |
| [[trello_request_read]] | Trello (`trello/account`) | no (GET/HEAD only) |
| [[trello_request_write]] | Trello | yes |

## Classification tags

| Tag | Use |
| --- | --- |
| `#mcp/tool` | Plugin tool note |
| `#api/request` | Plugin request note (`http` block) |
| `#api/service/*` | Authentication service: `atlassian`, `bitbucket`, `trello` |
| `#api/app/*` | App: `jira`, `jira-software`, `jsm`, `confluence`, `assets`, `automation`, `bitbucket`, `jsm-ops`, `forms`, `csm`, `admin`, `scim`, `trello` |
| `#api/resource/*` | API category (folder name in the official collection) |
| `#api/operation/*` | `list`, `get`, `search`, `create`, `update`, `delete`, `action` |
| `#api/effect/*` | `read` or `write` |
| `#api/permission/*` | `global-admin` or `project-admin` (detected from the official description) |
| `#api/version/*` | `v1` or `v2` (Confluence) |
| `#api/restriction/*` | `app-connect` (Connect/Forge apps only) or `oauth-devops` (requires OAuth/JWT) — kept as requests only |
| `#api/format/*` | `multipart` (upload) or `binary` (file/image) — kept as requests only |
| `#api/status/experimental` | Experimental endpoint (sends `X-ExperimentalApi: opt-in`) |

## Related notes
```dataview
LIST FROM [[]] WHERE contains(flat(list(up)), this.file.link)
SORT file.name ASC
```
