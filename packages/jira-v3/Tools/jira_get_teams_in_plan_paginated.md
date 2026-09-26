---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/teams-in-plan
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_teams_in_plan_paginated
title: "Jira v3 - Get teams in plan paginated"
kind: request
request: "[[Jira v3 - Get teams in plan paginated]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/plans/plan/{planId}/team · Get teams in plan paginated. Returns a paginated list of plan-only and Atlassian teams in a plan. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "planId":
    type: string
    required: true
    description: "The ID of the plan."
  "cursor":
    type: string
    required: false
    description: "The cursor to start from. If not provided, the first page will be returned."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of plan teams to return per page. The maximum value is 50. The default value is 50."
writes: false
expose: false
---
# jira_get_teams_in_plan_paginated

`GET /rest/api/3/plans/plan/{planId}/team` — Get teams in plan paginated

- Request: [[Jira v3 - Get teams in plan paginated]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
