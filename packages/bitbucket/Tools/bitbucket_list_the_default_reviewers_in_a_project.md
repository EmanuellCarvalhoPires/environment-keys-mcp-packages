---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/projects
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_the_default_reviewers_in_a_project
title: "Bitbucket - List the default reviewers in a project"
kind: request
request: "[[Bitbucket - List the default reviewers in a project]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/projects/{project_key}/default-reviewers · List the default reviewers in a project. Return a list of all default reviewers for a project. This is a list of users that will be added as default reviewers to pull requests for any repository within the project. Writes data: no."
params:
  "project_key":
    type: string
    required: true
    description: "Value of projectkey in the path."
writes: false
expose: false
---
# bitbucket_list_the_default_reviewers_in_a_project

`GET /workspaces/{workspace}/projects/{project_key}/default-reviewers` — List the default reviewers in a project

- Request: [[Bitbucket - List the default reviewers in a project]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
