---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/comment
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/attachments/{id}/footer-comments"
category: "Comment"
writes_data: false
tool_note: "[[confluence_get_attachment_comments]]"
---
# Confluence v2 - Get attachment comments

**Get attachment comments** — `GET /attachments/{id}/footer-comments`

- Run by the tool [[confluence_get_attachment_comments]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/attachments/{{param:id}}/footer-comments?body-format={{param:body_format}}&cursor={{param:cursor}}&limit={{param:limit}}&sort={{param:sort}}&version={{param:version}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the attachment for which comments should be returned.
- `body_format` (query, string, optional) — The content format type to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of comments per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results.
- `sort` (query, string, optional) — Used to sort the result by a particular field.
- `version` (query, string, optional) — Version number of the attachment to retrieve comments for. If no version provided, retrieves comments for the latest version.

## Original description

Returns the comments of the specific attachment.
The number of results is limited by the `limit` parameter and additional results (if available) will be available through
the `next` URL present in the `Link` response header.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the attachment and its corresponding containers.
