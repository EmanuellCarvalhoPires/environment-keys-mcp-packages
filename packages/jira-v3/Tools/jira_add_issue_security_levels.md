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
tool: jira_add_issue_security_levels
title: "Jira v3 - Add issue security levels"
kind: request
request: "[[Jira v3 - Add issue security levels]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issuesecurityschemes/{schemeId}/level · Add issue security levels. Adds levels and levels' members to the issue security scheme. You can add up to 100 levels per request. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "schemeId":
    type: string
    required: true
    description: "The ID of the issue security scheme."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_add_issue_security_levels

`PUT /rest/api/3/issuesecurityschemes/{schemeId}/level` — Add issue security levels

- Request: [[Jira v3 - Add issue security levels]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
