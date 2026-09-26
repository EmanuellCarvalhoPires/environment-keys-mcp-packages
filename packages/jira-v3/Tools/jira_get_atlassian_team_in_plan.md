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
tool: jira_get_atlassian_team_in_plan
title: "Jira v3 - Get Atlassian team in plan"
kind: request
request: "[[Jira v3 - Get Atlassian team in plan]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId} · Get Atlassian team in plan. Returns planning settings for an Atlassian team in a plan. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "planId":
    type: string
    required: true
    description: "The ID of the plan."
  "atlassianTeamId":
    type: string
    required: true
    description: "The ID of the Atlassian team."
writes: false
expose: false
---
# jira_get_atlassian_team_in_plan

`GET /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}` — Get Atlassian team in plan

- Request: [[Jira v3 - Get Atlassian team in plan]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
