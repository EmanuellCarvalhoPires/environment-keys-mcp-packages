---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_deploy_key_from_a_project
title: "Bitbucket - Delete a deploy key from a project"
kind: request
request: "[[Bitbucket - Delete a deploy key from a project]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id} · Delete a deploy key from a project. This deletes a deploy key from a project. Writes data: yes."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
  "key_id":
    type: string
    required: true
    description: "Value of keyid in the path."
writes: true
expose: false
---
# bitbucket_delete_a_deploy_key_from_a_project

`DELETE /workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id}` — Delete a deploy key from a project

- Request: [[Bitbucket - Delete a deploy key from a project]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
