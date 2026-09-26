---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/content/{id}/restriction"
category: "Content restrictions"
writes_data: false
tool_note: "[[confluence_v1_get_restrictions]]"
---
# Confluence v1 - Get restrictions

**Get restrictions** — `GET /wiki/rest/api/content/{id}/restriction`

- Run by the tool [[confluence_v1_get_restrictions]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/content/{{param:id}}/restriction?expand={{param:expand}}&start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the content to be queried for its restrictions.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the content restrictions to expand. By default, the following objects are expanded: restrictions.user, restrictions.group.
- `start` (query, string, optional) — The starting index of the users and groups in the returned restrictions.
- `limit` (query, string, optional) — The maximum number of users and the maximum number of groups, in the returned restrictions, to return per page. Note, this may be restricted by fixed system limits.

## Original description

Returns the restrictions on a piece of content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content.
