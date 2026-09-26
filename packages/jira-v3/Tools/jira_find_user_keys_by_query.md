---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_find_user_keys_by_query
title: "Jira v3 - Find user keys by query"
kind: request
request: "[[Jira v3 - Find user keys by query]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/user/search/query/key · Find user keys by query. Finds users with a structured query and returns a paginated list of user keys. This operation takes the users in the range defined by startAt and maxResults, up to the thousandth user, and then returns only the users from that range that match the structured query. Writes data: no."
params:
  "query":
    type: string
    required: true
    description: "The search query."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResult":
    type: string
    required: false
    description: "The maximum number of items to return per page."
writes: false
expose: false
---
# jira_find_user_keys_by_query

`GET /rest/api/3/user/search/query/key` — Find user keys by query

- Request: [[Jira v3 - Find user keys by query]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
