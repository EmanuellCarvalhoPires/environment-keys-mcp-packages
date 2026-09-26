---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/version
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/attachments/{id}/versions"
category: "Version"
writes_data: false
tool_note: "[[confluence_get_attachment_versions]]"
---
# Confluence v2 - Get attachment versions

**Get attachment versions** — `GET /attachments/{id}/versions`

- Run by the tool [[confluence_get_attachment_versions]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/attachments/{{param:id}}/versions?cursor={{param:cursor}}&limit={{param:limit}}&sort={{param:sort}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the attachment to be queried for its versions. If you don't know the attachment ID, use Get attachments and filter the results.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of versions per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.
- `sort` (query, string, optional) — Used to sort the result by a particular field.

## Original description

Returns the versions of specific attachment.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the attachment and its corresponding space.
