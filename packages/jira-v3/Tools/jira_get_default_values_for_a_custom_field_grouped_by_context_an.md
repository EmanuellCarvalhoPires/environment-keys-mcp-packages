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
tool: jira_get_default_values_for_a_custom_field_grouped_by_context_an
title: "Jira v3 - Get default values for a custom field grouped by context and issue type"
kind: request
request: "[[Jira v3 - Get default values for a custom field grouped by context and issue type]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/field/{fieldId}/context/defaultValues · Get default values for a custom field grouped by context and issue type. Returns a paginated list of default values grouped by custom field context. Each returned ContextDefaultValuesBean has a contextId and a defaultValues list of IssueTypeDefaultValueBean entries - one per issue-type-scoped default value configured for the context. Writes data: no."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the custom field, for example customfield\\10000."
  "contextId":
    type: string
    required: false
    description: "The IDs of the contexts to return default values for. If omitted, default values for every context the custom field has are returned."
  "issueTypeId":
    type: string
    required: false
    description: "The IDs of the issue types to restrict the returned per-issue-type default values to. If omitted, default values for every issue type are returned."
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
# jira_get_default_values_for_a_custom_field_grouped_by_context_an

`GET /rest/api/3/field/{fieldId}/context/defaultValues` — Get default values for a custom field grouped by context and issue type

- Request: [[Jira v3 - Get default values for a custom field grouped by context and issue type]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
