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
tool: jira_add_issue_types_to_context
title: "Jira v3 - Add issue types to context"
kind: request
request: "[[Jira v3 - Add issue types to context]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/field/{fieldId}/context/{contextId}/issuetype · Add issue types to context. Adds issue types to a custom field context, appending the issue types to the issue types list. A custom field context without any issue types applies to all issue types. Adding issue types to such a custom field context would result in it applying to only the listed issue types. Writes data: yes."
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
# jira_add_issue_types_to_context

`PUT /rest/api/3/field/{fieldId}/context/{contextId}/issuetype` — Add issue types to context

- Request: [[Jira v3 - Add issue types to context]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
