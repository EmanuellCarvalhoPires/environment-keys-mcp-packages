---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/source
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_the_root_directory_of_the_main_branch
title: "Bitbucket - Get the root directory of the main branch"
kind: request
request: "[[Bitbucket - Get the root directory of the main branch]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/src · Get the root directory of the main branch. This endpoint redirects the client to the directory listing of the root directory on the main branch. This is equivalent to directly hitting /2.0/repositories/{username}/{reposlug}/src/{commit}/{path} without having to know the name or SHA1 of the repo's main branch. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "format":
    type: string
    required: false
    description: "Instead of returning the file's contents, return the (json) meta data for it."
writes: false
expose: false
---
# bitbucket_get_the_root_directory_of_the_main_branch

`GET /repositories/{workspace}/{repo_slug}/src` — Get the root directory of the main branch

- Request: [[Bitbucket - Get the root directory of the main branch]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
