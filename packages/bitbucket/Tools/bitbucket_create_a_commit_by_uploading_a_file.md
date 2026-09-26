---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/source
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_commit_by_uploading_a_file
title: "Bitbucket - Create a commit by uploading a file"
kind: request
request: "[[Bitbucket - Create a commit by uploading a file]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/src · Create a commit by uploading a file. This endpoint is used to create new commits in the repository by uploading files. To add a new file to a repository: $ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \\ -F /repo/path/to/image.png=@image.png This will create a new commit on top of the main branch… Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "message":
    type: string
    required: false
    description: "The commit message. When omitted, Bitbucket uses a canned string."
  "author":
    type: string
    required: false
    description: "The raw string to be used as the new commit's author. This string follows the format Erik van Zijst ."
  "parents":
    type: string
    required: false
    description: "Deprecation Notice: Support for specifying multiple parent commits is deprecated and will be removed in a future release. Only a single SHA1 is accepted."
  "files":
    type: string
    required: false
    description: "Optional field that declares the files that the request is manipulating. When adding a new file to a repo, or when overwriting an existing file, the client can just upload the full contents of the fil…"
  "branch":
    type: string
    required: false
    description: "The name of the branch that the new commit should be created on. When omitted, the commit will be created on top of the main branch and will become the main branch's new head."
writes: true
expose: false
---
# bitbucket_create_a_commit_by_uploading_a_file

`POST /repositories/{workspace}/{repo_slug}/src` — Create a commit by uploading a file

- Request: [[Bitbucket - Create a commit by uploading a file]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
