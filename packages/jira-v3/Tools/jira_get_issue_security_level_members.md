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
tool: jira_get_issue_security_level_members
title: "Jira v3 - Get issue security level members"
kind: request
request: "[[Jira v3 - Get issue security level members]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuesecurityschemes/level/member · Get issue security level members. Returns a paginated list of issue security level members. Only issue security level members in the context of classic projects are returned. Writes data: no."
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
    description: "The list of issue security level member IDs. To include multiple issue security level members separate IDs with an ampersand: id=10000&id=10001."
  "schemeId":
    type: string
    required: false
    description: "The list of issue security scheme IDs. To include multiple issue security schemes separate IDs with an ampersand: schemeId=10000&schemeId=10001."
  "levelId":
    type: string
    required: false
    description: "The list of issue security level IDs. To include multiple issue security levels separate IDs with an ampersand: levelId=10000&levelId=10001."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list."
writes: false
expose: false
---
# jira_get_issue_security_level_members

`GET /rest/api/3/issuesecurityschemes/level/member` — Get issue security level members

- Request: [[Jira v3 - Get issue security level members]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
