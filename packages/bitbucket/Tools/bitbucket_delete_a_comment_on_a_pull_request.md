---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_comment_on_a_pull_request
title: "Bitbucket - Delete a comment on a pull request"
kind: request
request: "[[Bitbucket - Delete a comment on a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id} · Delete a comment on a pull request. Deletes a specific pull request comment. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "pull_request_id":
    type: string
    required: true
    description: "Value of pullrequestid in the path."
  "comment_id":
    type: string
    required: true
    description: "Value of commentid in the path."
writes: true
expose: false
---
# bitbucket_delete_a_comment_on_a_pull_request

`DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}` — Delete a comment on a pull request

- Request: [[Bitbucket - Delete a comment on a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
