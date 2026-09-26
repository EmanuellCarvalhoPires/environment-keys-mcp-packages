---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_search_issue_security_schemes
title: "Jira v3 - Search issue security schemes"
kind: request
request: "[[Jira v3 - Search issue security schemes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuesecurityschemes/search · Search issue security schemes. Returns a paginated list of issue security schemes. If you specify the project ID parameter, the result will contain issue security schemes and related project IDs you filter by. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "id":
    type: string
    required: false
    description: "The list of issue security scheme IDs. To include multiple issue security scheme IDs, separate IDs with an ampersand: id=10000&id=10001."
  "projectId":
    type: string
    required: false
    description: "The list of project IDs. To include multiple project IDs, separate IDs with an ampersand: projectId=10000&projectId=10001."
writes: false
expose: false
---
# jira_search_issue_security_schemes

`GET /rest/api/3/issuesecurityschemes/search` — Search issue security schemes

- Request: [[Jira v3 - Search issue security schemes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
