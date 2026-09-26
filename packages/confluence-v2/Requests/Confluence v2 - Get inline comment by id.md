---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/comment
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/inline-comments/{comment-id}"
category: "Comment"
writes_data: false
tool_note: "[[confluence_get_inline_comment_by_id]]"
---
# Confluence v2 - Get inline comment by id

**Get inline comment by id** — `GET /inline-comments/{comment-id}`

- Run by the tool [[confluence_get_inline_comment_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/inline-comments/{{param:comment_id}}?body-format={{param:body_format}}&version={{param:version}}&include-properties={{param:include_properties}}&include-operations={{param:include_operations}}&include-likes={{param:include_likes}}&include-versions={{param:include_versions}}&include-version={{param:include_version}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `comment_id` (path, string, required) — The ID of the comment to be retrieved.
- `body_format` (query, string, optional) — The content format type to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field.
- `version` (query, string, optional) — Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.
- `include_properties` (query, string, optional) — Includes content properties associated with this inline comment in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_operations` (query, string, optional) — Includes operations associated with this inline comment in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order.
- `include_likes` (query, string, optional) — Includes likes associated with this inline comment in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_versions` (query, string, optional) — Includes versions associated with this inline comment in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_version` (query, string, optional) — Includes the current version associated with this inline comment in the response. By default this is included and can be omitted by setting the value to false.

## Original description

Retrieves an inline comment by id

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content of the page or blogpost and its corresponding space.
