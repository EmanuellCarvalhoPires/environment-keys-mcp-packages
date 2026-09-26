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
tool: jira_validate_create_workflows
title: "Jira v3 - Validate create workflows"
kind: request
request: "[[Jira v3 - Validate create workflows]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/workflows/create/validation · Validate create workflows. Validate the payload for bulk create workflows. Permissions required: Administer Jira project permission to create all, including global-scoped, workflows Administer projects project permissions to create project-scoped workflows Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_validate_create_workflows

`POST /rest/api/3/workflows/create/validation` — Validate create workflows

- Request: [[Jira v3 - Validate create workflows]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
