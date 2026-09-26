---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-contexts
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_remove_custom_field_context_from_projects
title: "Jira v3 - Remove custom field context from projects"
kind: request
request: "[[Jira v3 - Remove custom field context from projects]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/field/{fieldId}/context/{contextId}/project/remove · Remove custom field context from projects. Removes a custom field context from projects. A custom field context without any projects applies to all projects. Removing all projects from a custom field context would result in it applying to all projects. Writes data: yes."
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
# jira_remove_custom_field_context_from_projects

`POST /rest/api/3/field/{fieldId}/context/{contextId}/project/remove` — Remove custom field context from projects

- Request: [[Jira v3 - Remove custom field context from projects]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
