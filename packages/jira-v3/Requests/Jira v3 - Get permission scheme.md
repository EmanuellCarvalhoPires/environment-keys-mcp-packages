---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/permission-schemes
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/permissionscheme/{schemeId}"
category: "Permission schemes"
writes_data: false
tool_note: "[[jira_get_permission_scheme]]"
---
# Jira v3 - Get permission scheme

**Get permission scheme** — `GET /rest/api/3/permissionscheme/{schemeId}`

- Run by the tool [[jira_get_permission_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/permissionscheme/{{param:schemeId}}?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `schemeId` (path, string, required) — The ID of the permission scheme to return.
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value.

## Original description

Returns a permission scheme.

**[Permissions](#permissions) required:** Permission to access Jira.
