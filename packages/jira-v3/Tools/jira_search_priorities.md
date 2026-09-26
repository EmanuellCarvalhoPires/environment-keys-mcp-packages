---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-priorities
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_search_priorities
title: "Jira v3 - Search priorities"
kind: request
request: "[[Jira v3 - Search priorities]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/priority/search · Search priorities. Returns a paginated list of priorities. The list can contain all priorities or a subset determined by any combination of these criteria: a list of priority IDs. Any invalid priority IDs are ignored. a list of project IDs. Writes data: no."
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
    description: "The list of priority IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=2&id=3."
  "projectId":
    type: string
    required: false
    description: "The list of projects IDs. To include multiple IDs, provide an ampersand-separated list. For example, projectId=10010&projectId=10111."
  "priorityName":
    type: string
    required: false
    description: "The name of priority to search for."
  "onlyDefault":
    type: string
    required: false
    description: "Whether only the default priority is returned."
  "expand":
    type: string
    required: false
    description: "Use schemes to return the associated priority schemes for each priority. Limited to returning first 15 priority schemes per priority."
writes: false
expose: false
---
# jira_search_priorities

`GET /rest/api/3/priority/search` — Search priorities

- Request: [[Jira v3 - Search priorities]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
