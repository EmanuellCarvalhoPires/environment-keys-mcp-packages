---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/user-properties
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_update_user_property
title: "Confluence v1 - Update user property"
kind: request
request: "[[Confluence v1 - Update user property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · PUT /wiki/rest/api/user/{userId}/property/{key} · Update user property. Updates a property for the given user. Note, you cannot update the key of a user property, only the value. For more information about user properties, see Confluence entity properties. Writes data: yes."
params:
  "userId":
    type: string
    required: true
    description: "The account ID of the user. The accountId uniquely identifies the user across all Atlassian products. For example, 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192"
  "key":
    type: string
    required: true
    description: "The key of the user property."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_update_user_property

`PUT /wiki/rest/api/user/{userId}/property/{key}` — Update user property

- Request: [[Confluence v1 - Update user property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
