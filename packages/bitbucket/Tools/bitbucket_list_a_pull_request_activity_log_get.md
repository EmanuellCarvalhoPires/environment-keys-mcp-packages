---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_a_pull_request_activity_log_get
title: "Bitbucket - List a pull request activity log (GET)"
kind: request
request: "[[Bitbucket - List a pull request activity log (GET)]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/activity · List a pull request activity log. Returns a paginated list of the pull request's activity log. This handler serves both a v20 and internal endpoint. The v20 endpoint returns reviewer comments, updates, approvals and request changes. The internal endpoint includes those plus tasks and attachments. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "pull_request_id":
    type: string
    required: true
    description: "Value of pullrequestid in the path."
writes: false
expose: false
---
# bitbucket_list_a_pull_request_activity_log_get

`GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/activity` — List a pull request activity log

- Request: [[Bitbucket - List a pull request activity log (GET)]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
