---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/search
  - api/effect/read
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_validate_update_workflows
title: "Jira v3 - Validate update workflows"
kind: request
request: "[[Jira v3 - Validate update workflows]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/workflows/update/validation · Validate update workflows. Validate the payload for bulk update workflows. Permissions required: Administer Jira project permission to create all, including global-scoped, workflows Administer projects project permissions to create project-scoped workflows Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_validate_update_workflows

`POST /rest/api/3/workflows/update/validation` — Validate update workflows

- Request: [[Jira v3 - Validate update workflows]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
