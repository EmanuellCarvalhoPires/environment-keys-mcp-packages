---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/downloads
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_download_artifacts
title: "Bitbucket - List download artifacts"
kind: request
request: "[[Bitbucket - List download artifacts]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/downloads · List download artifacts. Returns a list of download links associated with the repository. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: false
expose: false
---
# bitbucket_list_download_artifacts

`GET /repositories/{workspace}/{repo_slug}/downloads` — List download artifacts

- Request: [[Bitbucket - List download artifacts]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
