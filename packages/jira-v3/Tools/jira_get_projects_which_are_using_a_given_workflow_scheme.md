---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-schemes
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_projects_which_are_using_a_given_workflow_scheme
title: "Jira v3 - Get projects which are using a given workflow scheme"
kind: request
request: "[[Jira v3 - Get projects which are using a given workflow scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/workflowscheme/{workflowSchemeId}/projectUsages · Get projects which are using a given workflow scheme. Returns a page of projects using a given workflow scheme. Writes data: no."
params:
  "workflowSchemeId":
    type: string
    required: true
    description: "The workflow scheme ID"
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
# jira_get_projects_which_are_using_a_given_workflow_scheme

`GET /rest/api/3/workflowscheme/{workflowSchemeId}/projectUsages` — Get projects which are using a given workflow scheme

- Request: [[Jira v3 - Get projects which are using a given workflow scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
