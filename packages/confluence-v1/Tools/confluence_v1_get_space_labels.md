---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/experimental
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_space_labels
title: "Confluence v1 - Get Space Labels"
kind: request
request: "[[Confluence v1 - Get Space Labels]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/space/{spaceKey}/label · Get Space Labels. Returns a list of labels associated with a space. Can provide a prefix as well as other filters to select different types of labels. Writes data: no."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to get labels for."
  "prefix":
    type: string
    required: false
    description: "Filters the results to labels with the specified prefix. If this parameter is not specified, then labels with any prefix will be returned."
  "start":
    type: string
    required: false
    description: "The starting index of the returned labels."
  "limit":
    type: string
    required: false
    description: "The maximum number of labels to return per page. Note, this may be restricted by fixed system limits."
writes: false
expose: false
---
# confluence_v1_get_space_labels

`GET /wiki/rest/api/space/{spaceKey}/label` — Get Space Labels

- Request: [[Confluence v1 - Get Space Labels]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
