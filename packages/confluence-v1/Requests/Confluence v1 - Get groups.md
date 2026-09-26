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
path: "/wiki/rest/api/group"
category: "Group"
writes_data: false
tool_note: "[[confluence_v1_get_groups]]"
---
# Confluence v1 - Get groups

**Get groups** — `GET /wiki/rest/api/group`

- Run by the tool [[confluence_v1_get_groups]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/group?start={{param:start}}&limit={{param:limit}}&accessType={{param:accessType}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `start` (query, string, optional) — The starting index of the returned groups.
- `limit` (query, string, optional) — The maximum number of groups to return per page. Note, this may be restricted by fixed system limits.
- `accessType` (query, string, optional) — The group permission level for which to filter results.

## Original description

Returns all user groups. The returned groups are ordered alphabetically in
ascending order by group name.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
