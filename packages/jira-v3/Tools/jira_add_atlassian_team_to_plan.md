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
tool: jira_add_atlassian_team_to_plan
title: "Jira v3 - Add Atlassian team to plan"
kind: request
request: "[[Jira v3 - Add Atlassian team to plan]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/plans/plan/{planId}/team/atlassian · Add Atlassian team to plan. Adds an existing Atlassian team to a plan and configures their plannning settings. Permissions required: Administer Jira global permission. Writes data: yes."
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
# jira_add_atlassian_team_to_plan

`POST /rest/api/3/plans/plan/{planId}/team/atlassian` — Add Atlassian team to plan

- Request: [[Jira v3 - Add Atlassian team to plan]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
