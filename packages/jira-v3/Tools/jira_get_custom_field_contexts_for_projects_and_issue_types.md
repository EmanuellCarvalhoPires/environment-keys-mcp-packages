---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-contexts
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_custom_field_contexts_for_projects_and_issue_types
title: "Jira v3 - Get custom field contexts for projects and issue types"
kind: request
request: "[[Jira v3 - Get custom field contexts for projects and issue types]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/field/{fieldId}/context/mapping · Get custom field contexts for projects and issue types. Returns a paginated list of project and issue type mappings and, for each mapping, the ID of a custom field context that applies to the project and issue type. Writes data: no."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the custom field."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_get_custom_field_contexts_for_projects_and_issue_types

`POST /rest/api/3/field/{fieldId}/context/mapping` — Get custom field contexts for projects and issue types

- Request: [[Jira v3 - Get custom field contexts for projects and issue types]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
