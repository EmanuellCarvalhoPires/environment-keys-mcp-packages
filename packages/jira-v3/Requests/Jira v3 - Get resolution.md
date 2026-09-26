---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-resolutions
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/resolution/{id}"
category: "Issue resolutions"
writes_data: false
tool_note: "[[jira_get_resolution]]"
---
# Jira v3 - Get resolution

**Get resolution** — `GET /rest/api/3/resolution/{id}`

- Run by the tool [[jira_get_resolution]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/resolution/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the issue resolution value.

## Original description

Returns an issue resolution value.

**[Permissions](#permissions) required:** Permission to access Jira.
