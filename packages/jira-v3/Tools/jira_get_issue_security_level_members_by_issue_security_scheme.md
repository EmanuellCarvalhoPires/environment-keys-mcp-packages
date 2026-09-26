---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-level
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_security_level_members_by_issue_security_scheme
title: "Jira v3 - Get issue security level members by issue security scheme"
kind: request
request: "[[Jira v3 - Get issue security level members by issue security scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members · Get issue security level members by issue security scheme. Returns issue security level members. Only issue security level members in context of classic projects are returned. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "issueSecuritySchemeId":
    type: string
    required: true
    description: "The ID of the issue security scheme. Use the Get issue security schemes operation to get a list of issue security scheme IDs."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "issueSecurityLevelId":
    type: string
    required: false
    description: "The list of issue security level IDs. To include multiple issue security levels separate IDs with ampersand: issueSecurityLevelId=10000&issueSecurityLevelId=10001."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expand options include: all Returns all expandable information."
writes: false
expose: false
---
# jira_get_issue_security_level_members_by_issue_security_scheme

`GET /rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members` — Get issue security level members by issue security scheme

- Request: [[Jira v3 - Get issue security level members by issue security scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
