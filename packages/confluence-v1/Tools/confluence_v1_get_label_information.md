---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/label-info
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_label_information
title: "Confluence v1 - Get label information"
kind: request
request: "[[Confluence v1 - Get label information]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/label · Get label information. Returns label information and a list of contents associated with the label. Permissions required: Permission to access the Confluence site ('Can use' global permission). Only contents that the user is permitted to view is returned. Writes data: no."
params:
  "name":
    type: string
    required: true
    description: "Name of the label to query."
  "type":
    type: string
    required: false
    description: "The type of contents that are to be returned."
  "start":
    type: string
    required: false
    description: "The starting offset for the results."
  "limit":
    type: string
    required: false
    description: "The number of results to be returned."
writes: false
expose: false
---
# confluence_v1_get_label_information

`GET /wiki/rest/api/label` — Get label information

- Request: [[Confluence v1 - Get label information]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
