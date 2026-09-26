---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_search_field_scheme_fields
title: "Jira v3 - Search field scheme fields"
kind: request
request: "[[Jira v3 - Search field scheme fields]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/config/fieldschemes/{id}/fields · Search field scheme fields. Search for fields belonging to a given field association scheme. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The scheme ID to search for child fields"
  "startAt":
    type: string
    required: false
    description: "The starting index of the returned fields. Base index: 0."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of fields to return per page, maximum allowed value is 100."
  "fieldId":
    type: string
    required: false
    description: "The field IDs to filter by, if empty then all fields belonging to a field association scheme will be returned"
writes: false
expose: false
---
# jira_search_field_scheme_fields

`GET /rest/api/3/config/fieldschemes/{id}/fields` — Search field scheme fields

- Request: [[Jira v3 - Search field scheme fields]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
