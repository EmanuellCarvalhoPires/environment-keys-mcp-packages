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
tool: jira_get_issue_types_for_custom_field_context
title: "Jira v3 - Get issue types for custom field context"
kind: request
request: "[[Jira v3 - Get issue types for custom field context]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/field/{fieldId}/context/issuetypemapping · Get issue types for custom field context. Returns a paginated list of context to issue type mappings for a custom field. Mappings are returned for all contexts or a list of contexts. Mappings are ordered first by context ID and then by issue type ID. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the custom field."
  "contextId":
    type: string
    required: false
    description: "The ID of the context. To include multiple contexts, provide an ampersand-separated list. For example, contextId=10001&contextId=10002."
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
# jira_get_issue_types_for_custom_field_context

`GET /rest/api/3/field/{fieldId}/context/issuetypemapping` — Get issue types for custom field context

- Request: [[Jira v3 - Get issue types for custom field context]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
