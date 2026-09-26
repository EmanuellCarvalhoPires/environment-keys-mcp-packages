---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-options
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_custom_field_options_context
title: "Jira v3 - Create custom field options (context)"
kind: request
request: "[[Jira v3 - Create custom field options (context)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/field/{fieldId}/context/{contextId}/option · Create custom field options (context). Creates options and, where the custom select field is of the type Select List (cascading), cascading options for a custom select field. The options are added to a context of the field. Writes data: yes."
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
# jira_create_custom_field_options_context

`POST /rest/api/3/field/{fieldId}/context/{contextId}/option` — Create custom field options (context)

- Request: [[Jira v3 - Create custom field options (context)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
