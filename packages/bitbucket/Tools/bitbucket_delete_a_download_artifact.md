---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/downloads
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_download_artifact
title: "Bitbucket - Delete a download artifact"
kind: request
request: "[[Bitbucket - Delete a download artifact]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/downloads/{filename} · Delete a download artifact. Deletes the specified download artifact from the repository. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "filename":
    type: string
    required: true
    description: "Value of filename in the path."
writes: true
expose: false
---
# bitbucket_delete_a_download_artifact

`DELETE /repositories/{workspace}/{repo_slug}/downloads/{filename}` — Delete a download artifact

- Request: [[Bitbucket - Delete a download artifact]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
