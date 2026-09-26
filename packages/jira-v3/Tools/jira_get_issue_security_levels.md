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
tool: jira_get_issue_security_levels
title: "Jira v3 - Get issue security levels"
kind: request
request: "[[Jira v3 - Get issue security levels]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuesecurityschemes/level · Get issue security levels. Returns a paginated list of issue security levels. Only issue security levels in the context of classic projects are returned. Writes data: no."
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
    description: "The list of issue security scheme level IDs. To include multiple issue security levels, separate IDs with an ampersand: id=10000&id=10001."
  "schemeId":
    type: string
    required: false
    description: "The list of issue security scheme IDs. To include multiple issue security schemes, separate IDs with an ampersand: schemeId=10000&schemeId=10001."
  "onlyDefault":
    type: string
    required: false
    description: "When set to true, returns multiple default levels for each security scheme containing a default. If you provide scheme and level IDs not associated with the default, returns an empty page."
writes: false
expose: false
---
# jira_get_issue_security_levels

`GET /rest/api/3/issuesecurityschemes/level` — Get issue security levels

- Request: [[Jira v3 - Get issue security levels]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
