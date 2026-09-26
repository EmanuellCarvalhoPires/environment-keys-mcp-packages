---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/refs
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_tag
title: "Bitbucket - Create a tag"
kind: request
request: "[[Bitbucket - Create a tag]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/refs/tags · Create a tag. Creates a new annotated tag in the specified repository. The payload of the POST should consist of a JSON document that contains the name of the tag and the target hash. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_create_a_tag

`POST /repositories/{workspace}/{repo_slug}/refs/tags` — Create a tag

- Request: [[Bitbucket - Create a tag]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
