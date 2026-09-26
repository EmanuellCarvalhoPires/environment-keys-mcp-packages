---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-watches
  - api/operation/create
  - api/effect/write
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_add_content_watcher
title: "Confluence v1 - Add content watcher"
kind: request
request: "[[Confluence v1 - Add content watcher]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/user/watch/content/{contentId} · Add content watcher. Adds a user as a watcher to a piece of content. Choose the user by doing one of the following: - Specify a user via a query parameter: Use the accountId to identify the user. - Do not specify a user: The currently logged-in user will be used. Writes data: yes."
params:
  "contentId":
    type: string
    required: true
    description: "The ID of the content to add the watcher to."
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
# confluence_v1_add_content_watcher

`POST /wiki/rest/api/user/watch/content/{contentId}` — Add content watcher

- Request: [[Confluence v1 - Add content watcher]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
