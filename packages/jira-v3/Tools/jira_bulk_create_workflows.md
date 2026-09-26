---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/action
  - api/effect/write
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_bulk_create_workflows
title: "Jira v3 - Bulk create workflows"
kind: request
request: "[[Jira v3 - Bulk create workflows]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/workflows/create · Bulk create workflows. Create workflows and related statuses. Permissions required: Administer Jira project permission to create all, including global-scoped, workflows Administer projects project permissions to create project-scoped workflows Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_create_workflows

`POST /rest/api/3/workflows/create` — Bulk create workflows

- Request: [[Jira v3 - Bulk create workflows]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
