---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/search
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_commits_with_include_exclude
title: "Bitbucket - List commits with include exclude"
kind: request
request: "[[Bitbucket - List commits with include exclude]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/commits · List commits with include/exclude. Identical to GET /repositories/{workspace}/{reposlug}/commits, except that POST allows clients to place the include and exclude parameters in the request body to avoid URL length issues. Note that this resource does NOT support new commit creation. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: false
expose: false
---
# bitbucket_list_commits_with_include_exclude

`POST /repositories/{workspace}/{repo_slug}/commits` — List commits with include/exclude

- Request: [[Bitbucket - List commits with include exclude]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
