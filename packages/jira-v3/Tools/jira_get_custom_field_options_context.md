---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-options
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_custom_field_options_context
title: "Jira v3 - Get custom field options (context)"
kind: request
request: "[[Jira v3 - Get custom field options (context)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/field/{fieldId}/context/{contextId}/option · Get custom field options (context). Returns a paginated list of all custom field option for a context. Options are returned first then cascading options, in the order they display in Jira. This operation works for custom field options created in Jira or the operations from this resource. Writes data: no."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the custom field."
  "contextId":
    type: string
    required: true
    description: "The ID of the context."
  "optionId":
    type: string
    required: false
    description: "The ID of the option."
  "onlyOptions":
    type: string
    required: false
    description: "Whether only options are returned."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
writes: false
expose: false
---
# jira_get_custom_field_options_context

`GET /rest/api/3/field/{fieldId}/context/{contextId}/option` — Get custom field options (context)

- Request: [[Jira v3 - Get custom field options (context)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
