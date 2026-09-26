---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-options
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_custom_field_options_context
title: "Jira v3 - Delete custom field options (context)"
kind: request
request: "[[Jira v3 - Delete custom field options (context)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId} · Delete custom field options (context). Deletes a custom field option. Options with cascading options cannot be deleted without deleting the cascading options first. This operation works for custom field options created in Jira or the operations from this resource. Writes data: yes."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the custom field."
  "contextId":
    type: string
    required: true
    description: "The ID of the context from which an option should be deleted."
  "optionId":
    type: string
    required: true
    description: "The ID of the option to delete."
writes: true
expose: false
---
# jira_delete_custom_field_options_context

`DELETE /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}` — Delete custom field options (context)

- Request: [[Jira v3 - Delete custom field options (context)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
