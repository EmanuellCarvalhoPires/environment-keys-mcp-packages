---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_task_on_a_pull_request
title: "Bitbucket - Create a task on a pull request"
kind: request
request: "[[Bitbucket - Create a task on a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks · Create a task on a pull request. Creates a new pull request task. Returns the newly created pull request task. Tasks can optionally be created in relation to a comment specified by the comment's ID which will cause the task to appear below the comment on a pull request when viewed in Bitbucket. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "pull_request_id":
    type: string
    required: true
    description: "Value of pullrequestid in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_create_a_task_on_a_pull_request

`POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks` — Create a task on a pull request

- Request: [[Bitbucket - Create a task on a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
