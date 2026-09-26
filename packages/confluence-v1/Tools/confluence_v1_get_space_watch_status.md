---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-watches
  - api/operation/get
  - api/effect/read
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_space_watch_status
title: "Confluence v1 - Get space watch status"
kind: request
request: "[[Confluence v1 - Get space watch status]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/user/watch/space/{spaceKey} · Get space watch status. Returns whether a user is watching a space. Choose the user by doing one of the following: - Specify a user via a query parameter: Use the accountId to identify the user. - Do not specify a user: The currently logged-in user will be used. Writes data: no."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to be queried for whether the specified user is watching it."
  "key":
    type: string
    required: false
    description: "This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details."
  "username":
    type: string
    required: false
    description: "This parameter is no longer available and will be removed from the documentation soon. Use accountId instead. See the deprecation notice for details."
  "accountId":
    type: string
    required: false
    description: "The account ID of the user. The accountId uniquely identifies the user across all Atlassian products. For example, 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192."
writes: false
expose: false
---
# confluence_v1_get_space_watch_status

`GET /wiki/rest/api/user/watch/space/{spaceKey}` — Get space watch status

- Request: [[Confluence v1 - Get space watch status]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
