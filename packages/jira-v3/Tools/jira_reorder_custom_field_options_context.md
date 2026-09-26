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
tool: jira_reorder_custom_field_options_context
title: "Jira v3 - Reorder custom field options (context)"
kind: request
request: "[[Jira v3 - Reorder custom field options (context)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/field/{fieldId}/context/{contextId}/option/move · Reorder custom field options (context). Changes the order of custom field options or cascading options in a context. This operation works for custom field options created in Jira or the operations from this resource. Writes data: yes."
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
# jira_reorder_custom_field_options_context

`PUT /rest/api/3/field/{fieldId}/context/{contextId}/option/move` — Reorder custom field options (context)

- Request: [[Jira v3 - Reorder custom field options (context)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
