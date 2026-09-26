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
tool: jira_update_issue_security_scheme
title: "Jira v3 - Update issue security scheme"
kind: request
request: "[[Jira v3 - Update issue security scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issuesecurityschemes/{id} · Update issue security scheme. Updates the issue security scheme. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
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
# jira_update_issue_security_scheme

`PUT /rest/api/3/issuesecurityschemes/{id}` — Update issue security scheme

- Request: [[Jira v3 - Update issue security scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
