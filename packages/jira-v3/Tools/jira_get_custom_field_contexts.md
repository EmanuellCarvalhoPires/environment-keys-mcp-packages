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
tool: jira_get_custom_field_contexts
title: "Jira v3 - Get custom field contexts"
kind: request
request: "[[Jira v3 - Get custom field contexts]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/field/{fieldId}/context · Get custom field contexts. Returns a paginated list of contexts for a custom field. Contexts can be returned as follows: With no other parameters set, all contexts. By defining id only, all contexts from the list of IDs. Writes data: no."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the custom field."
  "isAnyIssueType":
    type: string
    required: false
    description: "Whether to return contexts that apply to all issue types."
  "isGlobalContext":
    type: string
    required: false
    description: "Whether to return contexts that apply to all projects."
  "contextId":
    type: string
    required: false
    description: "The list of context IDs. To include multiple contexts, separate IDs with ampersand: contextId=10000&contextId=10001."
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
# jira_get_custom_field_contexts

`GET /rest/api/3/field/{fieldId}/context` — Get custom field contexts

- Request: [[Jira v3 - Get custom field contexts]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
