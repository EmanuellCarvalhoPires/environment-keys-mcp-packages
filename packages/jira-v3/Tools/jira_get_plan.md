---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/plans
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_plan
title: "Jira v3 - Get plan"
kind: request
request: "[[Jira v3 - Get plan]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/plans/plan/{planId} · Get plan. Returns a plan. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "planId":
    type: string
    required: true
    description: "The ID of the plan."
  "useGroupId":
    type: string
    required: false
    description: "Whether to return group IDs instead of group names. Group names are deprecated."
writes: false
expose: false
---
# jira_get_plan

`GET /rest/api/3/plans/plan/{planId}` — Get plan

- Request: [[Jira v3 - Get plan]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
