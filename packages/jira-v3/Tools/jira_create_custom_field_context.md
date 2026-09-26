---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-contexts
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_custom_field_context
title: "Jira v3 - Create custom field context"
kind: request
request: "[[Jira v3 - Create custom field context]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/field/{fieldId}/context · Create custom field context. Creates a custom field context. If projectIds is empty, a global context is created. A global context is one that applies to all project. If issueTypeIds is empty, the context applies to all issue types. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the custom field."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_custom_field_context

`POST /rest/api/3/field/{fieldId}/context` — Create custom field context

- Request: [[Jira v3 - Create custom field context]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
