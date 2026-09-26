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
tool: jira_get_projects_with_field_schemes
title: "Jira v3 - Get projects with field schemes"
kind: request
request: "[[Jira v3 - Get projects with field schemes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/config/fieldschemes/projects · Get projects with field schemes. Get projects with field association schemes. This will be a temporary API but useful when transitioning from the legacy field configuration APIs to the new ones. Permissions required: Administer Jira global permission. Writes data: no."
params:
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
    required: true
    description: "List of project ids to filter the results by."
writes: false
expose: false
---
# jira_get_projects_with_field_schemes

`GET /rest/api/3/config/fieldschemes/projects` — Get projects with field schemes

- Request: [[Jira v3 - Get projects with field schemes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
