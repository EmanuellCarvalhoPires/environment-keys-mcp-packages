---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_project_deploy_key
title: "Bitbucket - Create a project deploy key"
kind: request
request: "[[Bitbucket - Create a project deploy key]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /workspaces/{workspace}/projects/{project_key}/deploy-keys · Create a project deploy key. Create a new deploy key in a project. Example: $ curl -X POST \\ -H \"Authorization \" \\ -H \"Content-type: application/json\" \\ https://api.bitbucket.org/2.0/workspaces/standard/projects/TESTPROJECT/deploy-keys/ -d \\ '{ \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JG… Writes data: yes."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
writes: true
expose: false
---
# bitbucket_create_a_project_deploy_key

`POST /workspaces/{workspace}/projects/{project_key}/deploy-keys` — Create a project deploy key

- Request: [[Bitbucket - Create a project deploy key]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
