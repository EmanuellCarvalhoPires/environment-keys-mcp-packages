---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/filter-sharing
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/filter/defaultShareScope"
category: "Filter sharing"
writes_data: true
tool_note: "[[jira_set_default_share_scope]]"
---
# Jira v3 - Set default share scope

**Set default share scope** — `PUT /rest/api/3/filter/defaultShareScope`

- Run by the tool [[jira_set_default_share_scope]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/filter/defaultShareScope
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "scope": "GLOBAL"
}
```

## Original description

Sets the default sharing for new filters and dashboards for a user.

**[Permissions](#permissions) required:** Permission to access Jira.
