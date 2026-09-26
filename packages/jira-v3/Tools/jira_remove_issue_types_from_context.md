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
tool: jira_remove_issue_types_from_context
title: "Jira v3 - Remove issue types from context"
kind: request
request: "[[Jira v3 - Remove issue types from context]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove · Remove issue types from context. Removes issue types from a custom field context. A custom field context without any issue types applies to all issue types. Permissions required: Administer Jira global permission. Writes data: yes."
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
# jira_remove_issue_types_from_context

`POST /rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove` — Remove issue types from context

- Request: [[Jira v3 - Remove issue types from context]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
