---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screens
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_screens_for_a_field
title: "Jira v3 - Get screens for a field"
kind: request
request: "[[Jira v3 - Get screens for a field]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/field/{fieldId}/screens · Get screens for a field. Returns a paginated list of the screens a field is used in. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the field to return screens for."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about screens in the response. This parameter accepts tab which returns details about the screen tabs the field is used in."
writes: false
expose: false
---
# jira_get_screens_for_a_field

`GET /rest/api/3/field/{fieldId}/screens` — Get screens for a field

- Request: [[Jira v3 - Get screens for a field]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
