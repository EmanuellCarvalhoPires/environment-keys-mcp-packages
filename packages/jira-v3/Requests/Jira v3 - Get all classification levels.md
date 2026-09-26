---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/classification-levels
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/classification-levels"
category: "Classification levels"
writes_data: false
tool_note: "[[jira_get_all_classification_levels]]"
---
# Jira v3 - Get all classification levels

**Get all classification levels** — `GET /rest/api/3/classification-levels`

- Run by the tool [[jira_get_all_classification_levels]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/classification-levels?status={{param:status}}&orderBy={{param:orderBy}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `status` (query, string, optional) — Optional set of statuses to filter by.
- `orderBy` (query, string, optional) — Ordering of the results by a given field. If not provided, values will not be sorted.

## Original description

Returns all classification levels.

**[Permissions](#permissions) required:** None.
