---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_projects_in_a_workspace
title: "Bitbucket - List projects in a workspace"
kind: request
request: "[[Bitbucket - List projects in a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/projects · List projects in a workspace. Returns the list of projects in this workspace. Writes data: no."
writes: false
expose: false
---
# bitbucket_list_projects_in_a_workspace

`GET /workspaces/{workspace}/projects` — List projects in a workspace

- Request: [[Bitbucket - List projects in a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
