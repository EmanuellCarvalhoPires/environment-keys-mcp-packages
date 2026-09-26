---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/plans
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_plan
title: "Jira v3 - Create plan"
kind: request
request: "[[Jira v3 - Create plan]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/plans/plan · Create plan. Creates a plan. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "useGroupId":
    type: string
    required: false
    description: "Whether to accept group IDs instead of group names. Group names are deprecated."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_plan

`POST /rest/api/3/plans/plan` — Create plan

- Request: [[Jira v3 - Create plan]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
