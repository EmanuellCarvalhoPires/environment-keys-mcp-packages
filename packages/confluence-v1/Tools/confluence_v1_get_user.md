---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/users
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_user
title: "Confluence v1 - Get user"
kind: request
request: "[[Confluence v1 - Get user]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/user · Get user. Returns a user. This includes information about the user, such as the display name, account ID, profile picture, and more. The information returned may be restricted by the user's profile visibility settings. Writes data: no."
params:
  "accountId":
    type: string
    required: true
    description: "The account ID of the user. The accountId uniquely identifies the user across all Atlassian products. For example, 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the user to expand. - operations returns the operations that the user is allowed to do."
writes: false
expose: false
---
# confluence_v1_get_user

`GET /wiki/rest/api/user` — Get user

- Request: [[Confluence v1 - Get user]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
