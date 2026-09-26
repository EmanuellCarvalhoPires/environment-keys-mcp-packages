---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/version
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_attachment_versions
title: "Confluence v2 - Get attachment versions"
kind: request
request: "[[Confluence v2 - Get attachment versions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /attachments/{id}/versions · Get attachment versions. Returns the versions of specific attachment. Permissions required: Permission to view the attachment and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the attachment to be queried for its versions. If you don't know the attachment ID, use Get attachments and filter the results."
  "cursor":
    type: string
    required: false
    description: "Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results."
  "limit":
    type: string
    required: false
    description: "Maximum number of versions per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results."
  "sort":
    type: string
    required: false
    description: "Used to sort the result by a particular field."
writes: false
expose: false
---
# confluence_get_attachment_versions

`GET /attachments/{id}/versions` — Get attachment versions

- Request: [[Confluence v2 - Get attachment versions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
