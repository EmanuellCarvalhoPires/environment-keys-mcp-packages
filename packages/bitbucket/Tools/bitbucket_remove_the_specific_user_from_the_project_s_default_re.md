---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_remove_the_specific_user_from_the_project_s_default_re
title: "Bitbucket - Remove the specific user from the project's default reviewers"
kind: request
request: "[[Bitbucket - Remove the specific user from the project's default reviewers]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user} · Remove the specific user from the project's default reviewers. Removes a default reviewer from the project. Example: $ curl https://api.bitbucket.org/2.0/.../default-reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D HTTP/1.1 204 Writes data: yes."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
  "selected_user":
    type: string
    required: true
    description: "Value of selecteduser in the path."
writes: true
expose: false
---
# bitbucket_remove_the_specific_user_from_the_project_s_default_re

`DELETE /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}` — Remove the specific user from the project's default reviewers

- Request: [[Bitbucket - Remove the specific user from the project's default reviewers]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
