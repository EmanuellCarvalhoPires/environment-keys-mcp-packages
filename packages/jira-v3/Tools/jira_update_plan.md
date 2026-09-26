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
tool: jira_update_plan
title: "Jira v3 - Update plan"
kind: request
request: "[[Jira v3 - Update plan]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/plans/plan/{planId} · Update plan. Updates any of the following details of a plan using JSON Patch. name leadAccountId scheduling estimation with StoryPoints, Days or Hours as possible values startDate type with DueDate, TargetStartDate, TargetEndDate or DateCustomField as possible values dateCustomFieldId endDate… Writes data: yes."
params:
  "planId":
    type: string
    required: true
    description: "The ID of the plan."
  "useGroupId":
    type: string
    required: false
    description: "Whether to accept group IDs instead of group names. Group names are deprecated."
  "body":
    type: array
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_plan

`PUT /rest/api/3/plans/plan/{planId}` — Update plan

- Request: [[Jira v3 - Update plan]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
