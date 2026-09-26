---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_workspace_pull_requests_for_a_user
title: "Bitbucket - List workspace pull requests for a user"
kind: request
request: "[[Bitbucket - List workspace pull requests for a user]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/pullrequests/{selected_user} · List workspace pull requests for a user. Returns all workspace pull requests authored by the specified user. By default only open pull requests are returned. This can be controlled using the state query parameter. Writes data: no."
params:
  "selected_user":
    type: string
    required: true
    description: "Value of selecteduser in the path."
  "state":
    type: string
    required: false
    description: "Only return pull requests that are in this state. This parameter can be repeated."
writes: false
expose: false
---
# bitbucket_list_workspace_pull_requests_for_a_user

`GET /workspaces/{workspace}/pullrequests/{selected_user}` — List workspace pull requests for a user

- Request: [[Bitbucket - List workspace pull requests for a user]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
