---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklogs
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_worklogs
title: "Jira v3 - Get issue worklogs"
kind: request
request: "[[Jira v3 - Get issue worklogs]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/{issueIdOrKey}/worklog · Get issue worklogs. Returns worklogs for an issue (ordered by created time), starting from the oldest worklog or from the worklog started on or after a date and time. Time tracking must be enabled in Jira, otherwise this operation returns an error. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "startedAfter":
    type: string
    required: false
    description: "The worklog start date and time, as a UNIX timestamp in milliseconds, after which worklogs are returned."
  "startedBefore":
    type: string
    required: false
    description: "The worklog start date and time, as a UNIX timestamp in milliseconds, before which worklogs are returned."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about worklogs in the response. This parameter acceptsproperties, which returns worklog properties."
writes: false
expose: false
---
# jira_get_issue_worklogs

`GET /rest/api/3/issue/{issueIdOrKey}/worklog` — Get issue worklogs

- Request: [[Jira v3 - Get issue worklogs]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
