---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/teams-in-plan
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_atlassian_team_in_plan
title: "Jira v3 - Update Atlassian team in plan"
kind: request
request: "[[Jira v3 - Update Atlassian team in plan]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId} · Update Atlassian team in plan. Updates any of the following planning settings of an Atlassian team in a plan using JSON Patch. planningStyle issueSourceId sprintLength capacity Permissions required: Administer Jira global permission. Note that \"add\" operations do not respect array indexes in target locations. Writes data: yes."
params:
  "planId":
    type: string
    required: true
    description: "The ID of the plan."
  "atlassianTeamId":
    type: string
    required: true
    description: "The ID of the Atlassian team."
  "body":
    type: array
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_atlassian_team_in_plan

`PUT /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}` — Update Atlassian team in plan

- Request: [[Jira v3 - Update Atlassian team in plan]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
