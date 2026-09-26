---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-options
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_custom_field_options_context
title: "Jira v3 - Update custom field options (context)"
kind: request
request: "[[Jira v3 - Update custom field options (context)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/field/{fieldId}/context/{contextId}/option · Update custom field options (context). Updates the options of a custom field. If any of the options are not found, no options are updated. Options where the values in the request match the current values aren't updated and aren't reported in the response. Writes data: yes."
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
# jira_update_custom_field_options_context

`PUT /rest/api/3/field/{fieldId}/context/{contextId}/option` — Update custom field options (context)

- Request: [[Jira v3 - Update custom field options (context)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
