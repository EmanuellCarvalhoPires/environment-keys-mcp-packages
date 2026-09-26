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
tool: jira_update_issue_security_level
title: "Jira v3 - Update issue security level"
kind: request
request: "[[Jira v3 - Update issue security level]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId} · Update issue security level. Updates the issue security level. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "schemeId":
    type: string
    required: true
    description: "The ID of the issue security scheme level belongs to."
  "levelId":
    type: string
    required: true
    description: "The ID of the issue security level to update."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_issue_security_level

`PUT /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}` — Update issue security level

- Request: [[Jira v3 - Update issue security level]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
