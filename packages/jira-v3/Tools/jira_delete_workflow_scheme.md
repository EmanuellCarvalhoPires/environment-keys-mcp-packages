---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_workflow_scheme
title: "Jira v3 - Delete workflow scheme"
kind: request
request: "[[Jira v3 - Delete workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/workflowscheme/{id} · Delete workflow scheme. Deletes a workflow scheme. Note that a workflow scheme cannot be deleted if it is active (that is, being used by at least one project). Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme. Find this ID by editing the desired workflow scheme in Jira. The ID is shown in the URL as schemeId. For example, schemeId=10301."
writes: true
expose: false
---
# jira_delete_workflow_scheme

`DELETE /rest/api/3/workflowscheme/{id}` — Delete workflow scheme

- Request: [[Jira v3 - Delete workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
