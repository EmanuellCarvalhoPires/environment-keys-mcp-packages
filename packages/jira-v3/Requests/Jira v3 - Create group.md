---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/groups
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/group"
category: "Groups"
writes_data: true
tool_note: "[[jira_create_group]]"
---
# Jira v3 - Create group

**Create group** — `POST /rest/api/3/group`

- Run by the tool [[jira_create_group]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/group
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "name": "power-users"
}
```

## Original description

Creates a group.

**[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).
