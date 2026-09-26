---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/attachment
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/attachments/{id}"
category: "Attachment"
writes_data: false
tool_note: "[[confluence_get_attachment_by_id]]"
---
# Confluence v2 - Get attachment by id

**Get attachment by id** — `GET /attachments/{id}`

- Run by the tool [[confluence_get_attachment_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/attachments/{{param:id}}?version={{param:version}}&include-labels={{param:include_labels}}&include-properties={{param:include_properties}}&include-operations={{param:include_operations}}&include-versions={{param:include_versions}}&include-version={{param:include_version}}&include-collaborators={{param:include_collaborators}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the attachment to be returned. If you don't know the attachment's ID, use Get attachments for page/blogpost/custom content.
- `version` (query, string, optional) — Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.
- `include_labels` (query, string, optional) — Includes labels associated with this attachment in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_properties` (query, string, optional) — Includes content properties associated with this attachment in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_operations` (query, string, optional) — Includes operations associated with this attachment in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order.
- `include_versions` (query, string, optional) — Includes versions associated with this attachment in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_version` (query, string, optional) — Includes the current version associated with this attachment in the response. By default this is included and can be omitted by setting the value to false.
- `include_collaborators` (query, string, optional) — Includes collaborators on the attachment.

## Original description

Returns a specific attachment.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the attachment's container.
