---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_webhook_for_a_workspace
title: "Bitbucket - Delete a webhook for a workspace"
kind: request
request: "[[Bitbucket - Delete a webhook for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /workspaces/{workspace}/hooks/{uid} · Delete a webhook for a workspace. Deletes the specified webhook subscription from the given workspace. Writes data: yes."
params:
  "uid":
    type: string
    required: true
    description: "Value of uid in the path."
writes: true
expose: false
---
# bitbucket_delete_a_webhook_for_a_workspace

`DELETE /workspaces/{workspace}/hooks/{uid}` — Delete a webhook for a workspace

- Request: [[Bitbucket - Delete a webhook for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
