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
tool: jira_update_custom_field_context
title: "Jira v3 - Update custom field context"
kind: request
request: "[[Jira v3 - Update custom field context]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/field/{fieldId}/context/{contextId} · Update custom field context. Updates a custom field context. Permissions required: Administer Jira global permission. Writes data: yes."
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
# jira_update_custom_field_context

`PUT /rest/api/3/field/{fieldId}/context/{contextId}` — Update custom field context

- Request: [[Jira v3 - Update custom field context]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
