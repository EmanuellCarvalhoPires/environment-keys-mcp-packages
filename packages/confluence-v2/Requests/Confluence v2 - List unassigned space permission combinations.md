---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-permission-transition
  - api/operation/list
  - api/effect/read
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/space-permissions/transition/combinations"
category: "Space Permission Transition"
writes_data: false
tool_note: "[[confluence_list_unassigned_space_permission_combinations]]"
---
# Confluence v2 - List unassigned space permission combinations

**List unassigned space permission combinations** — `GET /space-permissions/transition/combinations`

- Run by the tool [[confluence_list_unassigned_space_permission_combinations]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/space-permissions/transition/combinations?cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `cursor` (query, string, optional) — Opaque cursor returned from a previous page in the cursor field of the response. Omit for the first page.
- `limit` (query, string, optional) — The maximum number of combinations to return per page. Requests outside the supported range return 400.

## Original description

Lists the unique unassigned space permission combinations currently present on the tenant.
Combinations that already map to a space role are filtered out server-side. Each row carries
the decoded set of space permissions and the principal types that currently hold the
combination — these inform which `principalType` values are valid to include in the matching
bulk role-assignments request.

Results are always sorted by `principalCount` descending. Sort field and sort order are not
configurable; page size is controlled by the `limit` query parameter (default 25, min 1,
max 250). Use the `cursor` field to page through additional results. The `generatedAt` field
reflects the last audit run that populated the combinations table — call the
generate-combinations endpoint to refresh stale data.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
User must be a Confluence administrator.
