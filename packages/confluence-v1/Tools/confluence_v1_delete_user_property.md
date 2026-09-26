---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/user-properties
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_delete_user_property
title: "Confluence v1 - Delete user property"
kind: request
request: "[[Confluence v1 - Delete user property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/user/{userId}/property/{key} · Delete user property. Deletes a property for the given user. For more information about user properties, see Confluence entity properties. Note, these properties stored against a user are on a Confluence site level and not space/content level. Writes data: yes."
params:
  "userId":
    type: string
    required: true
    description: "The account ID of the user. The accountId uniquely identifies the user across all Atlassian products. For example, 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192"
  "key":
    type: string
    required: true
    description: "The key of the user property."
writes: true
expose: false
---
# confluence_v1_delete_user_property

`DELETE /wiki/rest/api/user/{userId}/property/{key}` — Delete user property

- Request: [[Confluence v1 - Delete user property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
