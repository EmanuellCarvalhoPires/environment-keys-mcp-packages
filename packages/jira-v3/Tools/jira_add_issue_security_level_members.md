---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_add_issue_security_level_members
title: "Jira v3 - Add issue security level members"
kind: request
request: "[[Jira v3 - Add issue security level members]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member · Add issue security level members. Adds members to the issue security level. You can add up to 100 members per request. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "schemeId":
    type: string
    required: true
    description: "The ID of the issue security scheme."
  "levelId":
    type: string
    required: true
    description: "The ID of the issue security level."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_add_issue_security_level_members

`PUT /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member` — Add issue security level members

- Request: [[Jira v3 - Add issue security level members]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
