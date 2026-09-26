---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-contexts
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_assign_custom_field_context_to_projects
title: "Jira v3 - Assign custom field context to projects"
kind: request
request: "[[Jira v3 - Assign custom field context to projects]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/field/{fieldId}/context/{contextId}/project · Assign custom field context to projects. Assigns a custom field context to projects. If any project in the request is assigned to any context of the custom field, the operation fails. This API will not allow adding projects to the global context from April 2026. Instead, an HTTP 400 response will be returned. Writes data: yes."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the custom field."
  "contextId":
    type: string
    required: true
    description: "The ID of the context."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_assign_custom_field_context_to_projects

`PUT /rest/api/3/field/{fieldId}/context/{contextId}/project` — Assign custom field context to projects

- Request: [[Jira v3 - Assign custom field context to projects]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
