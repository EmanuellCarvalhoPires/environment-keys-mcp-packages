---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/labels
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_all_labels
title: "Jira v3 - Get all labels"
kind: request
request: "[[Jira v3 - Get all labels]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/label · Get all labels. Returns a paginated list of labels. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
writes: false
expose: false
---
# jira_get_all_labels

`GET /rest/api/3/label` — Get all labels

- Request: [[Jira v3 - Get all labels]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
