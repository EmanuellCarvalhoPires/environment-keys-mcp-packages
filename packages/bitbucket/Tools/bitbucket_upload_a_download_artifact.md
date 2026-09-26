---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/downloads
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_upload_a_download_artifact
title: "Bitbucket - Upload a download artifact"
kind: request
request: "[[Bitbucket - Upload a download artifact]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/downloads · Upload a download artifact. Upload new download artifacts. To upload files, perform a multipart/form-data POST containing one or more files fields: $ echo Hello World hello.txt $ curl -s -u evzijst -X POST https://api.bitbucket.org/2.0/repositories/evzijst/git-tests/downloads -F files=@hello.txt When a file… Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: true
expose: false
---
# bitbucket_upload_a_download_artifact

`POST /repositories/{workspace}/{repo_slug}/downloads` — Upload a download artifact

- Request: [[Bitbucket - Upload a download artifact]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
