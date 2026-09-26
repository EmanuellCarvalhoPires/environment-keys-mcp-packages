---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-contexts
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_custom_field_context
title: "Jira v3 - Delete custom field context"
kind: request
request: "[[Jira v3 - Delete custom field context]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/field/{fieldId}/context/{contextId} · Delete custom field context. Deletes a custom field context. This API will not allow removing the global context from April 2026. Instead, an HTTP 400 response will be returned. See CHANGE-3019 Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the custom field."
  "contextId":
    type: string
    required: true
    description: "The ID of the context."
writes: true
expose: false
---
# jira_delete_custom_field_context

`DELETE /rest/api/3/field/{fieldId}/context/{contextId}` — Delete custom field context

- Request: [[Jira v3 - Delete custom field context]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
