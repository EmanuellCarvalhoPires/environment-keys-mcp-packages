---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/teams-in-plan
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_remove_atlassian_team_from_plan
title: "Jira v3 - Remove Atlassian team from plan"
kind: request
request: "[[Jira v3 - Remove Atlassian team from plan]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId} · Remove Atlassian team from plan. Removes an Atlassian team from a plan and deletes their planning settings. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "planId":
    type: string
    required: true
    description: "The ID of the plan."
  "atlassianTeamId":
    type: string
    required: true
    description: "The ID of the Atlassian team."
writes: true
expose: false
---
# jira_remove_atlassian_team_from_plan

`DELETE /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}` — Remove Atlassian team from plan

- Request: [[Jira v3 - Remove Atlassian team from plan]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
