---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_classic_update_workflow_scheme
title: "Jira v3 - Classic update workflow scheme"
kind: request
request: "[[Jira v3 - Classic update workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/workflowscheme/{id} · Classic update workflow scheme. Updates a company-manged project workflow scheme, including the name, default workflow, issue type to project mappings, and more. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme. Find this ID by editing the desired workflow scheme in Jira. The ID is shown in the URL as schemeId. For example, schemeId=10301."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_classic_update_workflow_scheme

`PUT /rest/api/3/workflowscheme/{id}` — Classic update workflow scheme

- Request: [[Jira v3 - Classic update workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
