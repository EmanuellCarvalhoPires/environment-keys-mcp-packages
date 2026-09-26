---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/refs
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_tag
title: "Bitbucket - Delete a tag"
kind: request
request: "[[Bitbucket - Delete a tag]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/refs/tags/{name} · Delete a tag. Delete a tag in the specified repository. The tag name should not include any prefixes (e.g. refs/tags). Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "name":
    type: string
    required: true
    description: "Value of name in the path."
writes: true
expose: false
---
# bitbucket_delete_a_tag

`DELETE /repositories/{workspace}/{repo_slug}/refs/tags/{name}` — Delete a tag

- Request: [[Bitbucket - Delete a tag]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
