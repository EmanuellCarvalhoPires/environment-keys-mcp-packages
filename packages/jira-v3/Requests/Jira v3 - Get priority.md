---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-priorities
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/priority/{id}"
category: "Issue priorities"
writes_data: false
tool_note: "[[jira_get_priority]]"
---
# Jira v3 - Get priority

**Get priority** — `GET /rest/api/3/priority/{id}`

- Run by the tool [[jira_get_priority]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/priority/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the issue priority.

## Original description

Returns an issue priority. To fetch multiple priorities at once, use [Search priorities](#api-rest-api-3-priority-search-get) instead.

**[Permissions](#permissions) required:** Permission to access Jira.
