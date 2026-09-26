---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-resolutions
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_search_resolutions
title: "Jira v3 - Search resolutions"
kind: request
request: "[[Jira v3 - Search resolutions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/resolution/search · Search resolutions. Returns a paginated list of resolutions. The list can contain all resolutions or a subset determined by any combination of these criteria: a list of resolutions IDs. whether the field configuration is a default. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "id":
    type: string
    required: false
    description: "The list of resolutions IDs to be filtered out"
  "onlyDefault":
    type: string
    required: false
    description: "When set to true, return default only, when IDs provided, if none of them is default, return empty page. Default value is false"
writes: false
expose: false
---
# jira_search_resolutions

`GET /rest/api/3/resolution/search` — Search resolutions

- Request: [[Jira v3 - Search resolutions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
