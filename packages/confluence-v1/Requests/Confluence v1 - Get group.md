---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/group
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/group/by-id"
category: "Group"
writes_data: false
tool_note: "[[confluence_v1_get_group]]"
---
# Confluence v1 - Get group

**Get group** — `GET /wiki/rest/api/group/by-id`

- Run by the tool [[confluence_v1_get_group]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/group/by-id?id={{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (query, string, required) — The id of the group.

## Original description

Returns a user group for a given group id.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
