---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_limit_report
title: "Jira v3 - Get issue limit report"
kind: request
request: "[[Jira v3 - Get issue limit report]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/limit/report · Get issue limit report. Returns all issues breaching and approaching per-issue limits. Permissions required: Browse projects project permission is required for the project the issues are in. Results may be incomplete otherwise Administer Jira global permission. Writes data: no."
params:
  "isReturningKeys":
    type: string
    required: false
    description: "Return issue keys instead of issue ids in the response. Usage: Add ?isReturningKeys=true to the end of the path to request issue keys."
writes: false
expose: false
---
# jira_get_issue_limit_report

`GET /rest/api/3/issue/limit/report` — Get issue limit report

- Request: [[Jira v3 - Get issue limit report]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
