---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_project_in_a_workspace
title: "Bitbucket - Create a project in a workspace"
kind: request
request: "[[Bitbucket - Create a project in a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /workspaces/{workspace}/projects · Create a project in a workspace. Creates a new project. Note that the avatar has to be embedded as either a data-url or a URL to an external image as shown in the examples below: $ body=$(cat << EOF { \"name\": \"Mars Project\", \"key\": \"MARS\", \"description\": \"Software for colonizing mars.\", \"links\": { \"avatar\": { \"h… Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_create_a_project_in_a_workspace

`POST /workspaces/{workspace}/projects` — Create a project in a workspace

- Request: [[Bitbucket - Create a project in a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
