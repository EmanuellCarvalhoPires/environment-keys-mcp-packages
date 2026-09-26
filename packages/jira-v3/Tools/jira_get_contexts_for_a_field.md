---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_contexts_for_a_field
title: "Jira v3 - Get contexts for a field"
kind: request
request: "[[Jira v3 - Get contexts for a field]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/field/{fieldId}/contexts · Get contexts for a field. Returns a paginated list of the contexts a field is used in. Deprecated, use Get custom field contexts. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the field to return contexts for."
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
# jira_get_contexts_for_a_field

`GET /rest/api/3/field/{fieldId}/contexts` — Get contexts for a field

- Request: [[Jira v3 - Get contexts for a field]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
