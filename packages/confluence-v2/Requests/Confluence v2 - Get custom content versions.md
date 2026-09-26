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
path: "/custom-content/{custom-content-id}/versions"
category: "Version"
writes_data: false
tool_note: "[[confluence_get_custom_content_versions]]"
---
# Confluence v2 - Get custom content versions

**Get custom content versions** — `GET /custom-content/{custom-content-id}/versions`

- Run by the tool [[confluence_get_custom_content_versions]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/custom-content/{{param:custom_content_id}}/versions?body-format={{param:body_format}}&cursor={{param:cursor}}&limit={{param:limit}}&sort={{param:sort}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `custom_content_id` (path, string, required) — The ID of the custom content to be queried for its versions. If you don't know the custom content ID, use Get custom-content by type and filter the results.
- `body_format` (query, string, optional) — The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of versions per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.
- `sort` (query, string, optional) — Used to sort the result by a particular field.

## Original description

Returns the versions of specific custom content.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the custom content and its corresponding page and space.
