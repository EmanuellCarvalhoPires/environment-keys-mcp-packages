---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/source
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_file_or_directory_contents
title: "Bitbucket - Get file or directory contents"
kind: request
request: "[[Bitbucket - Get file or directory contents]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/src/{commit}/{path} · Get file or directory contents. This endpoints is used to retrieve the contents of a single file, or the contents of a directory at a specified revision. Raw file contents When path points to a file, this endpoint returns the raw contents. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "commit":
    type: string
    required: true
    description: "Value of commit in the path."
  "path":
    type: string
    required: true
    description: "Value of path in the path."
  "format":
    type: string
    required: false
    description: "If 'meta' is provided, returns the (json) meta data for the contents of the file. If 'rendered' is provided, returns the contents of a non-binary file in HTML-formatted rendered markup."
  "q":
    type: string
    required: false
    description: "Optional filter expression as per filtering and sorting."
  "sort":
    type: string
    required: false
    description: "Optional sorting parameter as per filtering and sorting."
  "max_depth":
    type: string
    required: false
    description: "If provided, returns the contents of the repository and its subdirectories recursively until the specified maxdepth of nested directories. When omitted, this defaults to 1."
writes: false
expose: false
---
# bitbucket_get_file_or_directory_contents

`GET /repositories/{workspace}/{repo_slug}/src/{commit}/{path}` — Get file or directory contents

- Request: [[Bitbucket - Get file or directory contents]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
