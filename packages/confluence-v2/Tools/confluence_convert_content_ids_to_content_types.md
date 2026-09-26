---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content
  - api/operation/search
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_convert_content_ids_to_content_types
title: "Confluence v2 - Convert content ids to content types"
kind: request
request: "[[Confluence v2 - Convert content ids to content types]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /content/convert-ids-to-types · Convert content ids to content types. Converts a list of content ids into their associated content types. This is useful for users migrating from v1 to v2 who may have stored just content ids without their associated type. This will return types as they should be used in v2. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# confluence_convert_content_ids_to_content_types

`POST /content/convert-ids-to-types` — Convert content ids to content types

- Request: [[Confluence v2 - Convert content ids to content types]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
