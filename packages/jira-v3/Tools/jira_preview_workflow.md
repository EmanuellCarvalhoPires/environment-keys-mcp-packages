---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_preview_workflow
title: "Jira v3 - Preview workflow"
kind: request
request: "[[Jira v3 - Preview workflow]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/workflows/preview · Preview workflow. Returns a requested workflow within a given project. The response provides a read-only preview of the workflow, omitting full configuration details. Permissions required: At least one of the Administer projects and View (read-only) workflow project permissions Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_preview_workflow

`POST /rest/api/3/workflows/preview` — Preview workflow

- Request: [[Jira v3 - Preview workflow]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
