---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_tasks_on_a_pull_request
title: "Bitbucket - List tasks on a pull request"
kind: request
request: "[[Bitbucket - List tasks on a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks · List tasks on a pull request. Returns a paginated list of the pull request's tasks. This endpoint supports filtering and sorting of the results by the 'task' field. See filtering and sorting for more details. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "pull_request_id":
    type: string
    required: true
    description: "Value of pullrequestid in the path."
  "q":
    type: string
    required: false
    description: "Query string to narrow down the response. See filtering and sorting for details."
  "sort":
    type: string
    required: false
    description: "Field by which the results should be sorted as per filtering and sorting. Defaults to createdon."
  "pagelen":
    type: string
    required: false
    description: "Current number of objects on the existing page. The default value is 10 with 100 being the maximum allowed value. Individual APIs may enforce different values."
writes: false
expose: false
---
# bitbucket_list_tasks_on_a_pull_request

`GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks` — List tasks on a pull request

- Request: [[Bitbucket - List tasks on a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
