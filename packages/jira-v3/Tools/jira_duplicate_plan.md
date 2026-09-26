---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/plans
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_duplicate_plan
title: "Jira v3 - Duplicate plan"
kind: request
request: "[[Jira v3 - Duplicate plan]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/plans/plan/{planId}/duplicate · Duplicate plan. Duplicates a plan. Permissions required: Administer Jira global permission. Writes data: yes."
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
# jira_duplicate_plan

`POST /rest/api/3/plans/plan/{planId}/duplicate` — Duplicate plan

- Request: [[Jira v3 - Duplicate plan]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
