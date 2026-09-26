---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/downloads
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_download_artifact_link
title: "Bitbucket - Get a download artifact link"
kind: request
request: "[[Bitbucket - Get a download artifact link]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/downloads/{filename} · Get a download artifact link. Return a redirect to the contents of a download artifact. This endpoint returns the actual file contents and not the artifact's metadata. $ curl -s -L https://api.bitbucket.org/2.0/repositories/evzijst/git-tests/downloads/hello.txt Hello World Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "filename":
    type: string
    required: true
    description: "Value of filename in the path."
writes: false
expose: false
---
# bitbucket_get_a_download_artifact_link

`GET /repositories/{workspace}/{repo_slug}/downloads/{filename}` — Get a download artifact link

- Request: [[Bitbucket - Get a download artifact link]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
