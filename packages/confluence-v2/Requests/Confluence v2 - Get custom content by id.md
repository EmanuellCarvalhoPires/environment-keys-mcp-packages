---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/custom-content
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/custom-content/{id}"
category: "Custom Content"
writes_data: false
tool_note: "[[confluence_get_custom_content_by_id]]"
---
# Confluence v2 - Get custom content by id

**Get custom content by id** — `GET /custom-content/{id}`

- Run by the tool [[confluence_get_custom_content_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/custom-content/{{param:id}}?body-format={{param:body_format}}&version={{param:version}}&include-labels={{param:include_labels}}&include-properties={{param:include_properties}}&include-operations={{param:include_operations}}&include-versions={{param:include_versions}}&include-version={{param:include_version}}&include-collaborators={{param:include_collaborators}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the custom content to be returned. If you don't know the custom content ID, use Get Custom Content by Type and filter the results.
- `body_format` (query, string, optional) — The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field.
- `version` (query, string, optional) — Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.
- `include_labels` (query, string, optional) — Includes labels associated with this custom content in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_properties` (query, string, optional) — Includes content properties associated with this custom content in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_operations` (query, string, optional) — Includes operations associated with this custom content in the response, as defined in the Operation object. The number of results will be limited to 50 and sorted in the default sort order.
- `include_versions` (query, string, optional) — Includes versions associated with this custom content in the response. The number of results will be limited to 50 and sorted in the default sort order.
- `include_version` (query, string, optional) — Includes the current version associated with this custom content in the response. By default this is included and can be omitted by setting the value to false.
- `include_collaborators` (query, string, optional) — Includes collaborators on the custom content.

## Original description

Returns a specific piece of custom content. 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the custom content, the container of the custom content, and the corresponding space (if different from the container).
