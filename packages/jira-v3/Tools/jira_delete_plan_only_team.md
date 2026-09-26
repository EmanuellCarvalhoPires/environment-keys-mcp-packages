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
tool: jira_delete_plan_only_team
title: "Jira v3 - Delete plan-only team"
kind: request
request: "[[Jira v3 - Delete plan-only team]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId} · Delete plan-only team. Deletes a plan-only team and their planning settings. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "planId":
    type: string
    required: true
    description: "The ID of the plan."
  "planOnlyTeamId":
    type: string
    required: true
    description: "The ID of the plan-only team."
writes: true
expose: false
---
# jira_delete_plan_only_team

`DELETE /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}` — Delete plan-only team

- Request: [[Jira v3 - Delete plan-only team]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
