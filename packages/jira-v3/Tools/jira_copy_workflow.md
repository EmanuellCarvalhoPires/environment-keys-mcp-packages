---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_copy_workflow
title: "Jira v3 - Copy workflow"
kind: request
request: "[[Jira v3 - Copy workflow]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/workflows/copy · Copy workflow. Copies an existing workflow, and the statuses it uses, into a new workflow with the given name. The copy is created in the same scope as the workflow it is copied from. If no description is provided, the copy is created with an empty description. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_copy_workflow

`POST /rest/api/3/workflows/copy` — Copy workflow

- Request: [[Jira v3 - Copy workflow]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
