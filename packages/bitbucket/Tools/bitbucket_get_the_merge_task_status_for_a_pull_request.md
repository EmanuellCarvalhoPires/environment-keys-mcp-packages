---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_the_merge_task_status_for_a_pull_request
title: "Bitbucket - Get the merge task status for a pull request"
kind: request
request: "[[Bitbucket - Get the merge task status for a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge/task-status/{task_id} · Get the merge task status for a pull request. When merging a pull request takes too long, the client receives a task ID along with a 202 status code. The task ID can be used in a call to this endpoint to check the status of a merge task. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "pull_request_id":
    type: string
    required: true
    description: "Value of pullrequestid in the path."
  "task_id":
    type: string
    required: true
    description: "Value of taskid in the path."
writes: false
expose: false
---
# bitbucket_get_the_merge_task_status_for_a_pull_request

`GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge/task-status/{task_id}` — Get the merge task status for a pull request

- Request: [[Bitbucket - Get the merge task status for a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
