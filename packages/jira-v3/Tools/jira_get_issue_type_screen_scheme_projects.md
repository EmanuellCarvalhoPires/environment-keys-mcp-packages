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
tool: jira_get_issue_type_screen_scheme_projects
title: "Jira v3 - Get issue type screen scheme projects"
kind: request
request: "[[Jira v3 - Get issue type screen scheme projects]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/project · Get issue type screen scheme projects. Returns a paginated list of projects associated with an issue type screen scheme. Only company-managed projects associated with an issue type screen scheme are returned. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "issueTypeScreenSchemeId":
    type: string
    required: true
    description: "The ID of the issue type screen scheme."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "query":
    type: string
    required: false
    description: "Query parameter query."
writes: false
expose: false
---
# jira_get_issue_type_screen_scheme_projects

`GET /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/project` — Get issue type screen scheme projects

- Request: [[Jira v3 - Get issue type screen scheme projects]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
