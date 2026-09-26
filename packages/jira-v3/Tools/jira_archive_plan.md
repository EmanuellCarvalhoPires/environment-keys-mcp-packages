---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/plans
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_archive_plan
title: "Jira v3 - Archive plan"
kind: request
request: "[[Jira v3 - Archive plan]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/plans/plan/{planId}/archive · Archive plan. Archives a plan. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "planId":
    type: string
    required: true
    description: "The ID of the plan."
writes: true
expose: false
---
# jira_archive_plan

`PUT /rest/api/3/plans/plan/{planId}/archive` — Archive plan

- Request: [[Jira v3 - Archive plan]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
