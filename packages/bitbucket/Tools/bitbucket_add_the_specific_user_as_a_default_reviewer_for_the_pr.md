---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_add_the_specific_user_as_a_default_reviewer_for_the_pr
title: "Bitbucket - Add the specific user as a default reviewer for the project"
kind: request
request: "[[Bitbucket - Add the specific user as a default reviewer for the project]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user} · Add the specific user as a default reviewer for the project. Adds the specified user to the project's list of default reviewers. The method is idempotent. Accepts an optional body containing the uuid of the user to be added. Writes data: yes."
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
# bitbucket_add_the_specific_user_as_a_default_reviewer_for_the_pr

`PUT /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}` — Add the specific user as a default reviewer for the project

- Request: [[Bitbucket - Add the specific user as a default reviewer for the project]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
