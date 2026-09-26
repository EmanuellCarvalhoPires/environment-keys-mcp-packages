---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/user-properties
  - api/operation/create
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_create_user_property_by_key
title: "Confluence v1 - Create user property by key"
kind: request
request: "[[Confluence v1 - Create user property by key]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/user/{userId}/property/{key} · Create user property by key. Creates a property for a user. For more information about user properties, see [Confluence entity properties] (https://developer.atlassian.com/cloud/confluence/confluence-entity-properties/). Writes data: yes."
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
# confluence_v1_create_user_property_by_key

`POST /wiki/rest/api/user/{userId}/property/{key}` — Create user property by key

- Request: [[Confluence v1 - Create user property by key]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
