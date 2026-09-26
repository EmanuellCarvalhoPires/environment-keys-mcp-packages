---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_inactive_workflow
title: "Jira v3 - Delete inactive workflow"
kind: request
request: "[[Jira v3 - Delete inactive workflow]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/workflow/{entityId} · Delete inactive workflow. Deletes a workflow. The workflow cannot be deleted if it is: an active workflow. a system workflow. associated with any workflow scheme. associated with any draft workflow scheme. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "entityId":
    type: string
    required: true
    description: "The entity ID of the workflow."
writes: true
expose: false
---
# jira_delete_inactive_workflow

`DELETE /rest/api/3/workflow/{entityId}` — Delete inactive workflow

- Request: [[Jira v3 - Delete inactive workflow]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
