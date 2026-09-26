---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-contexts
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_custom_field_contexts_default_values
title: "Jira v3 - Get custom field contexts default values"
kind: request
request: "[[Jira v3 - Get custom field contexts default values]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/field/{fieldId}/context/defaultValue · Get custom field contexts default values. Returns a paginated list of defaults for a custom field. The results can be filtered by contextId, otherwise all values are returned. If no defaults are set for a context, nothing is returned. Writes data: no."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the custom field, for example customfield\\10000."
  "contextId":
    type: string
    required: false
    description: "The IDs of the contexts."
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
# jira_get_custom_field_contexts_default_values

`GET /rest/api/3/field/{fieldId}/context/defaultValue` — Get custom field contexts default values

- Request: [[Jira v3 - Get custom field contexts default values]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
