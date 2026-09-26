---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_bulk_get_workflows
title: "Jira v3 - Bulk get workflows"
kind: request
request: "[[Jira v3 - Bulk get workflows]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/workflows · Bulk get workflows. Returns a list of workflows and related statuses by providing workflow names, workflow IDs, or project and issue types. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_bulk_get_workflows

`POST /rest/api/3/workflows` — Bulk get workflows

- Request: [[Jira v3 - Bulk get workflows]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
