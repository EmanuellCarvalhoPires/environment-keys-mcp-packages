---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/user-properties
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_user_properties
title: "Confluence v1 - Get user properties"
kind: request
request: "[[Confluence v1 - Get user properties]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/user/{userId}/property · Get user properties. Returns the properties for a user as list of property keys. For more information about user properties, see Confluence entity properties. Note, these properties stored against a user are on a Confluence site level and not space/content level. Writes data: no."
params:
  "userId":
    type: string
    required: true
    description: "The account ID of the user to be queried for its properties."
  "start":
    type: string
    required: false
    description: "The starting index of the returned properties."
  "limit":
    type: string
    required: false
    description: "The maximum number of properties to return per page. Note, this may be restricted by fixed system limits."
writes: false
expose: false
---
# confluence_v1_get_user_properties

`GET /wiki/rest/api/user/{userId}/property` — Get user properties

- Request: [[Confluence v1 - Get user properties]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
