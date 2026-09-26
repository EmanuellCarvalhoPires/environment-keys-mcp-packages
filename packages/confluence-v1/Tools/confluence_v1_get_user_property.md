---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/user-properties
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_user_property
title: "Confluence v1 - Get user property"
kind: request
request: "[[Confluence v1 - Get user property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/user/{userId}/property/{key} · Get user property. Returns the property corresponding to key for a user. For more information about user properties, see Confluence entity properties. Note, these properties stored against a user are on a Confluence site level and not space/content level. Writes data: no."
params:
  "userId":
    type: string
    required: true
    description: "The account ID of the user to be queried for its properties."
  "key":
    type: string
    required: true
    description: "The key of the user property."
writes: false
expose: false
---
# confluence_v1_get_user_property

`GET /wiki/rest/api/user/{userId}/property/{key}` — Get user property

- Request: [[Confluence v1 - Get user property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
