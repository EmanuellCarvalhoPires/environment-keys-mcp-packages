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
path: "/wiki/rest/api/group/{groupId}/membersByGroupId"
category: "Group"
writes_data: false
tool_note: "[[confluence_v1_get_group_members]]"
---
# Confluence v1 - Get group members

**Get group members** — `GET /wiki/rest/api/group/{groupId}/membersByGroupId`

- Run by the tool [[confluence_v1_get_group_members]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/group/{{param:groupId}}/membersByGroupId?start={{param:start}}&limit={{param:limit}}&shouldReturnTotalSize={{param:shouldReturnTotalSize}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `groupId` (path, string, required) — The id of the group to be queried for its members.
- `start` (query, string, optional) — The starting index of the returned users.
- `limit` (query, string, optional) — The maximum number of users to return per page. Note, this may be restricted by fixed system limits.
- `shouldReturnTotalSize` (query, string, optional) — Whether to include total size parameter in the results. Note, fetching total size property is an expensive operation; use it if your use case needs this value.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the user to expand. - operations returns the operations that the user is allowed to do.

## Original description

Returns the users that are members of a group.

Use updated Get group API

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
