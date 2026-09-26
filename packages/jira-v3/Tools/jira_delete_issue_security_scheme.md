---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_issue_security_scheme
title: "Jira v3 - Delete issue security scheme"
kind: request
request: "[[Jira v3 - Delete issue security scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issuesecurityschemes/{schemeId} · Delete issue security scheme. Deletes an issue security scheme. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "schemeId":
    type: string
    required: true
    description: "The ID of the issue security scheme."
writes: true
expose: false
---
# jira_delete_issue_security_scheme

`DELETE /rest/api/3/issuesecurityschemes/{schemeId}` — Delete issue security scheme

- Request: [[Jira v3 - Delete issue security scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
