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
tool: jira_update_plan_only_team
title: "Jira v3 - Update plan-only team"
kind: request
request: "[[Jira v3 - Update plan-only team]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId} · Update plan-only team. Updates any of the following planning settings of a plan-only team using JSON Patch. name planningStyle issueSourceId sprintLength capacity memberAccountIds Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "planId":
    type: string
    required: true
    description: "The ID of the plan."
  "planOnlyTeamId":
    type: string
    required: true
    description: "The ID of the plan-only team."
  "body":
    type: array
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_plan_only_team

`PUT /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}` — Update plan-only team

- Request: [[Jira v3 - Update plan-only team]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
