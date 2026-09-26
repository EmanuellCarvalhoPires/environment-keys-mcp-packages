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
tool: jira_get_project_mappings_for_custom_field_context
title: "Jira v3 - Get project mappings for custom field context"
kind: request
request: "[[Jira v3 - Get project mappings for custom field context]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/field/{fieldId}/context/projectmapping · Get project mappings for custom field context. Returns a paginated list of context to project mappings for a custom field. The result can be filtered by contextId. Otherwise, all mappings are returned. Invalid IDs are ignored. Note: Jira is adding support for multiple field contexts per project. Writes data: no."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the custom field, for example customfield\\10000."
  "contextId":
    type: string
    required: false
    description: "The list of context IDs. To include multiple context, separate IDs with ampersand: contextId=10000&contextId=10001."
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
# jira_get_project_mappings_for_custom_field_context

`GET /rest/api/3/field/{fieldId}/context/projectmapping` — Get project mappings for custom field context

- Request: [[Jira v3 - Get project mappings for custom field context]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
