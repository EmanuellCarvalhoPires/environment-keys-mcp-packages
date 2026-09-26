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
tool: jira_trash_plan
title: "Jira v3 - Trash plan"
kind: request
request: "[[Jira v3 - Trash plan]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/plans/plan/{planId}/trash · Trash plan. Moves a plan to trash. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "planId":
    type: string
    required: true
    description: "The ID of the plan."
writes: true
expose: false
---
# jira_trash_plan

`PUT /rest/api/3/plans/plan/{planId}/trash` — Trash plan

- Request: [[Jira v3 - Trash plan]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
