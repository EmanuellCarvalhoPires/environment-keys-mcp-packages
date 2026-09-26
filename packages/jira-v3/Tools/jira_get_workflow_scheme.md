---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_workflow_scheme
title: "Jira v3 - Get workflow scheme"
kind: request
request: "[[Jira v3 - Get workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflowscheme/{id} · Get workflow scheme. Returns a workflow scheme. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme. Find this ID by editing the desired workflow scheme in Jira. The ID is shown in the URL as schemeId. For example, schemeId=10301."
  "returnDraftIfExists":
    type: string
    required: false
    description: "Returns the workflow scheme's draft rather than scheme itself, if set to true. If the workflow scheme does not have a draft, then the workflow scheme is returned."
writes: false
expose: false
---
# jira_get_workflow_scheme

`GET /rest/api/3/workflowscheme/{id}` — Get workflow scheme

- Request: [[Jira v3 - Get workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
