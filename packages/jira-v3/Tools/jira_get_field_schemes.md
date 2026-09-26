---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_field_schemes
title: "Jira v3 - Get field schemes"
kind: request
request: "[[Jira v3 - Get field schemes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/config/fieldschemes · Get field schemes. REST endpoint for retrieving a paginated list of field association schemes with optional filtering. This endpoint allows clients to fetch field association schemes with optional filtering by project IDs and text queries. Writes data: no."
params:
  "projectId":
    type: string
    required: false
    description: "(optional) List of project IDs to filter schemes by. If not provided, schemes from all projects are returned."
  "query":
    type: string
    required: false
    description: "(optional) Text filter for scheme name or description matching (case-insensitive). If not provided, no text filtering is applied."
  "startAt":
    type: string
    required: false
    description: "Zero-based index of the first item to return (default: 0)"
  "maxResults":
    type: string
    required: false
    description: "Maximum number of items to return per page (default: 50, max: 100)"
writes: false
expose: false
---
# jira_get_field_schemes

`GET /rest/api/3/config/fieldschemes` — Get field schemes

- Request: [[Jira v3 - Get field schemes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
