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
tool: jira_search_field_scheme_projects
title: "Jira v3 - Search field scheme projects"
kind: request
request: "[[Jira v3 - Search field scheme projects]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/config/fieldschemes/{id}/projects · Search field scheme projects. REST Endpoint for searching for projects belonging to a given field association scheme Permissions required: Administer Jira global permission. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The scheme id to search for associated projects"
  "startAt":
    type: string
    required: false
    description: "The starting index of the returned projects. Base index: 0."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of projects to return per page, maximum allowed value is 100."
  "projectId":
    type: string
    required: false
    description: "The project Ids to filter by, if empty then all projects belonging to a field association scheme will be returned"
writes: false
expose: false
---
# jira_search_field_scheme_projects

`GET /rest/api/3/config/fieldschemes/{id}/projects` — Search field scheme projects

- Request: [[Jira v3 - Search field scheme projects]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
