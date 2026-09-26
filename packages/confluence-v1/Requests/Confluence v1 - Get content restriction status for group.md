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
path: "/wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}"
category: "Content restrictions"
writes_data: false
tool_note: "[[confluence_v1_get_content_restriction_status_for_group]]"
---
# Confluence v1 - Get content restriction status for group

**Get content restriction status for group** — `GET /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}`

- Run by the tool [[confluence_v1_get_content_restriction_status_for_group]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/content/{{param:id}}/restriction/byOperation/{{param:operationKey}}/byGroupId/{{param:groupId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the content that the restriction applies to.
- `operationKey` (path, string, required) — The operation that the restriction applies to.
- `groupId` (path, string, required) — The id of the group to be queried for whether the content restriction applies to it.

## Original description

Returns whether the specified content restriction applies to a group.
For example, if a page with `id=123` has a `read` restriction for the `123456` group id,
the following request will return `true`:

`/wiki/rest/api/content/123/restriction/byOperation/read/byGroupId/123456`

Note that a response of `true` does not guarantee that the group can view the page, as it does not account for
account-inherited restrictions, space permissions, or even product access. For more
information, see [Confluence permissions](https://confluence.atlassian.com/x/_AozKw).

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content.
