---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklogs
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_ids_of_deleted_worklogs
title: "Jira v3 - Get IDs of deleted worklogs"
kind: request
request: "[[Jira v3 - Get IDs of deleted worklogs]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/worklog/deleted · Get IDs of deleted worklogs. Returns a list of IDs and delete timestamps for worklogs deleted after a date and time. This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. Writes data: no."
params:
  "since":
    type: string
    required: false
    description: "The date and time, as a UNIX timestamp in milliseconds, after which deleted worklogs are returned."
writes: false
expose: false
---
# jira_get_ids_of_deleted_worklogs

`GET /rest/api/3/worklog/deleted` — Get IDs of deleted worklogs

- Request: [[Jira v3 - Get IDs of deleted worklogs]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
