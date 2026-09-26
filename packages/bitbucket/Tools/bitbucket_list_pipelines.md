---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_pipelines
title: "Bitbucket - List pipelines"
kind: request
request: "[[Bitbucket - List pipelines]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines · List pipelines. Find pipelines in a repository. Note that unlike other endpoints in the Bitbucket API, this endpoint utilizes query parameters to allow filtering and sorting of returned results. See query parameters for specific details. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "creator_uuid":
    type: string
    required: false
    description: "The UUID of the creator of the pipeline to filter by."
  "target_ref_type":
    type: string
    required: false
    description: "The type of the reference to filter by."
  "target_ref_name":
    type: string
    required: false
    description: "The reference name to filter by."
  "target_branch":
    type: string
    required: false
    description: "The name of the branch to filter by."
  "target_commit_hash":
    type: string
    required: false
    description: "The revision to filter by."
  "target_selector_pattern":
    type: string
    required: false
    description: "The pipeline pattern to filter by."
  "target_selector_type":
    type: string
    required: false
    description: "The type of pipeline to filter by."
  "created_on":
    type: string
    required: false
    description: "The creation date to filter by."
  "trigger_type":
    type: string
    required: false
    description: "The trigger type to filter by."
  "status":
    type: string
    required: false
    description: "The pipeline status to filter by."
  "sort":
    type: string
    required: false
    description: "The attribute name to sort on."
  "page":
    type: string
    required: false
    description: "The page number of elements to retrieve."
  "pagelen":
    type: string
    required: false
    description: "The maximum number of results to return."
writes: false
expose: false
---
# bitbucket_list_pipelines

`GET /repositories/{workspace}/{repo_slug}/pipelines` — List pipelines

- Request: [[Bitbucket - List pipelines]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
