---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_fields_for_projects
title: "Jira v3 - Get fields for projects"
kind: request
request: "[[Jira v3 - Get fields for projects]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/projects/fields · Get fields for projects. Returns a paginated list of fields for the requested projects and work types. Only fields that are available for the specified combination of projects and work types are returned. This endpoint allows filtering to specific fields if field IDs are provided. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "projectId":
    type: string
    required: true
    description: "The IDs of projects to return fields for."
  "workTypeId":
    type: string
    required: true
    description: "The IDs of work types (issue types) to return fields for."
  "fieldId":
    type: string
    required: false
    description: "The IDs of fields to return. If not provided, all fields are returned."
writes: false
expose: false
---
# jira_get_fields_for_projects

`GET /rest/api/3/projects/fields` — Get fields for projects

- Request: [[Jira v3 - Get fields for projects]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
