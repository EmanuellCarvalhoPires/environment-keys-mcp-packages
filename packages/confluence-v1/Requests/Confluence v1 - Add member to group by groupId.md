---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/group
  - api/operation/create
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/group/userByGroupId"
category: "Group"
writes_data: true
tool_note: "[[confluence_v1_add_member_to_group_by_groupid]]"
---
# Confluence v1 - Add member to group by groupId

**Add member to group by groupId** — `POST /wiki/rest/api/group/userByGroupId`

- Run by the tool [[confluence_v1_add_member_to_group_by_groupid]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/group/userByGroupId?groupId={{param:groupId}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `groupId` (query, string, required) — GroupId of the group whose membership is updated
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Adds a user as a member in a group represented by its groupId

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
User must be a site admin.
