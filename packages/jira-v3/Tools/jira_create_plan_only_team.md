---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/teams-in-plan
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_plan_only_team
title: "Jira v3 - Create plan-only team"
kind: request
request: "[[Jira v3 - Create plan-only team]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/plans/plan/{planId}/team/planonly · Create plan-only team. Creates a plan-only team and configures their planning settings. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "planId":
    type: string
    required: true
    description: "The ID of the plan."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_plan_only_team

`POST /rest/api/3/plans/plan/{planId}/team/planonly` — Create plan-only team

- Request: [[Jira v3 - Create plan-only team]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
