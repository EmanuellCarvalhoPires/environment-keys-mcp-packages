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
tool: jira_set_workflow_for_issue_type_in_workflow_scheme
title: "Jira v3 - Set workflow for issue type in workflow scheme"
kind: request
request: "[[Jira v3 - Set workflow for issue type in workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/workflowscheme/{id}/issuetype/{issueType} · Set workflow for issue type in workflow scheme. Sets the workflow for an issue type in a workflow scheme. Note that active workflow schemes cannot be edited. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the workflow scheme."
  "issueType":
    type: string
    required: true
    description: "The ID of the issue type."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_workflow_for_issue_type_in_workflow_scheme

`PUT /rest/api/3/workflowscheme/{id}/issuetype/{issueType}` — Set workflow for issue type in workflow scheme

- Request: [[Jira v3 - Set workflow for issue type in workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
