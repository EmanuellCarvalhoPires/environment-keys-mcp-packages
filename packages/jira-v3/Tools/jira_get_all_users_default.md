---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/users
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_all_users_default
title: "Jira v3 - Get all users default"
kind: request
request: "[[Jira v3 - Get all users default]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/users · Get all users default. Returns a list of all users, including active users, inactive users and previously deleted users that have an Atlassian account. Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return (limited to 1000)."
  "expand":
    type: string
    required: false
    description: "Query parameter expand."
writes: false
expose: false
---
# jira_get_all_users_default

`GET /rest/api/3/users` — Get all users default

- Request: [[Jira v3 - Get all users default]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
