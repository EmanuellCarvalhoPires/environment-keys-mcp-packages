---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_projects_using_issue_security_schemes
title: "Jira v3 - Get projects using issue security schemes"
kind: request
request: "[[Jira v3 - Get projects using issue security schemes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuesecurityschemes/project · Get projects using issue security schemes. Returns a paginated mapping of projects that are using security schemes. You can provide either one or multiple security scheme IDs or project IDs to filter by. If you don't provide any, this will return a list of all mappings. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "issueSecuritySchemeId":
    type: string
    required: false
    description: "The list of security scheme IDs to be filtered out."
  "projectId":
    type: string
    required: false
    description: "The list of project IDs to be filtered out."
writes: false
expose: false
---
# jira_get_projects_using_issue_security_schemes

`GET /rest/api/3/issuesecurityschemes/project` — Get projects using issue security schemes

- Request: [[Jira v3 - Get projects using issue security schemes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
