---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/teams-in-plan
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_plan_only_team
title: "Jira v3 - Get plan-only team"
kind: request
request: "[[Jira v3 - Get plan-only team]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId} · Get plan-only team. Returns planning settings for a plan-only team. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "planId":
    type: string
    required: true
    description: "The ID of the plan."
  "planOnlyTeamId":
    type: string
    required: true
    description: "The ID of the plan-only team."
writes: false
expose: false
---
# jira_get_plan_only_team

`GET /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}` — Get plan-only team

- Request: [[Jira v3 - Get plan-only team]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
