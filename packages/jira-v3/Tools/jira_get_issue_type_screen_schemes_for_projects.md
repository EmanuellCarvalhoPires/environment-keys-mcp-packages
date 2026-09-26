---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-screen-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_type_screen_schemes_for_projects
title: "Jira v3 - Get issue type screen schemes for projects"
kind: request
request: "[[Jira v3 - Get issue type screen schemes for projects]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuetypescreenscheme/project · Get issue type screen schemes for projects. Returns a paginated list of issue type screen schemes and, for each issue type screen scheme, a list of the projects that use it. Only issue type screen schemes used in classic projects are returned. Permissions required: Administer Jira global permission. Writes data: no."
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
    description: "The list of project IDs. To include multiple projects, separate IDs with ampersand: projectId=10000&projectId=10001."
writes: false
expose: false
---
# jira_get_issue_type_screen_schemes_for_projects

`GET /rest/api/3/issuetypescreenscheme/project` — Get issue type screen schemes for projects

- Request: [[Jira v3 - Get issue type screen schemes for projects]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
