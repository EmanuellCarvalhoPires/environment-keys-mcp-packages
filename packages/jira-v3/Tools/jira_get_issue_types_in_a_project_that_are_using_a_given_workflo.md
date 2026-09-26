---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_types_in_a_project_that_are_using_a_given_workflo
title: "Jira v3 - Get issue types in a project that are using a given workflow"
kind: request
request: "[[Jira v3 - Get issue types in a project that are using a given workflow]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflow/{workflowId}/project/{projectId}/issueTypeUsages · Get issue types in a project that are using a given workflow. Returns a page of issue types using a given workflow within a project. Writes data: no."
params:
  "workflowId":
    type: string
    required: true
    description: "The workflow ID"
  "projectId":
    type: string
    required: true
    description: "The project ID"
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
# jira_get_issue_types_in_a_project_that_are_using_a_given_workflo

`GET /rest/api/3/workflow/{workflowId}/project/{projectId}/issueTypeUsages` — Get issue types in a project that are using a given workflow

- Request: [[Jira v3 - Get issue types in a project that are using a given workflow]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
