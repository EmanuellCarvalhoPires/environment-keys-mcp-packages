---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-watches
  - api/operation/delete
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_remove_space_watch
title: "Confluence v1 - Remove space watch"
kind: request
request: "[[Confluence v1 - Remove space watch]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/user/watch/space/{spaceKey} · Remove space watch. Removes a user as a watcher from a space. Choose the user by doing one of the following: - Specify a user via a query parameter: Use the accountId to identify the user. - Do not specify a user: The currently logged-in user will be used. Writes data: yes."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to remove the watcher from."
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
writes: true
expose: false
---
# confluence_v1_remove_space_watch

`DELETE /wiki/rest/api/user/watch/space/{spaceKey}` — Remove space watch

- Request: [[Confluence v1 - Remove space watch]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
