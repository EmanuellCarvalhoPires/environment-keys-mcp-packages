---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}"
category: "Content restrictions"
writes_data: false
tool_note: "[[confluence_v1_get_restrictions_for_operation]]"
---
# Confluence v1 - Get restrictions for operation

**Get restrictions for operation** — `GET /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}`

- Run by the tool [[confluence_v1_get_restrictions_for_operation]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/content/{{param:id}}/restriction/byOperation/{{param:operationKey}}?expand={{param:expand}}&start={{param:start}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the content to be queried for its restrictions.
- `operationKey` (path, string, required) — The operation type of the restrictions to be returned.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the content restrictions to expand. - restrictions.user returns the piece of content that the restrictions are applied to. Expanded by default.
- `start` (query, string, optional) — The starting index of the users and groups in the returned restrictions.
- `limit` (query, string, optional) — The maximum number of users and the maximum number of groups, in the returned restrictions, to return per page. Note, this may be restricted by fixed system limits.

## Original description

Returns the restictions on a piece of content for a given operation (read
or update).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content.
