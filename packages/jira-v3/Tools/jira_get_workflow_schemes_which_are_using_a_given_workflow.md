---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_workflow_schemes_which_are_using_a_given_workflow
title: "Jira v3 - Get workflow schemes which are using a given workflow"
kind: request
request: "[[Jira v3 - Get workflow schemes which are using a given workflow]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflow/{workflowId}/workflowSchemes · Get workflow schemes which are using a given workflow. Returns a page of workflow schemes using a given workflow. Writes data: no."
params:
  "workflowId":
    type: string
    required: true
    description: "The workflow ID"
  "nextPageToken":
    type: string
    required: false
    description: "The cursor for pagination"
  "maxResults":
    type: string
    required: false
    description: "The maximum number of results to return. Must be an integer between 1 and 200."
writes: false
expose: false
---
# jira_get_workflow_schemes_which_are_using_a_given_workflow

`GET /rest/api/3/workflow/{workflowId}/workflowSchemes` — Get workflow schemes which are using a given workflow

- Request: [[Jira v3 - Get workflow schemes which are using a given workflow]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
