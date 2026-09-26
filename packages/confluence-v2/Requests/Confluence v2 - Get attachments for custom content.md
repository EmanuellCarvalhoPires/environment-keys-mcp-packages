---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/attachment
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/custom-content/{id}/attachments"
category: "Attachment"
writes_data: false
tool_note: "[[confluence_get_attachments_for_custom_content]]"
---
# Confluence v2 - Get attachments for custom content

**Get attachments for custom content** — `GET /custom-content/{id}/attachments`

- Run by the tool [[confluence_get_attachments_for_custom_content]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/custom-content/{{param:id}}/attachments?sort={{param:sort}}&cursor={{param:cursor}}&status={{param:status}}&mediaType={{param:mediaType}}&filename={{param:filename}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the custom content for which attachments should be returned.
- `sort` (query, string, optional) — Used to sort the result by a particular field.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `status` (query, string, optional) — Filter the results to attachments based on their status. By default, current and archived are used.
- `mediaType` (query, string, optional) — Filters on the mediaType of attachments. Only one may be specified.
- `filename` (query, string, optional) — Filters on the file-name of attachments. Only one may be specified.
- `limit` (query, string, optional) — Maximum number of attachments per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.

## Original description

Returns the attachments of specific custom content. The number of results is limited by the `limit` parameter and additional results (if available)
will be available through the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content of the custom content and its corresponding space.
