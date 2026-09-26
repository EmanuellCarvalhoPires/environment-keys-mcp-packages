---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_security_scheme
title: "Jira v3 - Get issue security scheme"
kind: request
request: "[[Jira v3 - Get issue security scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuesecurityschemes/{id} · Get issue security scheme. Returns an issue security scheme along with its security levels. Permissions required: Administer Jira global permission. Administer Projects project permission for a project that uses the requested issue security scheme. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the issue security scheme. Use the Get issue security schemes operation to get a list of issue security scheme IDs."
writes: false
expose: false
---
# jira_get_issue_security_scheme

`GET /rest/api/3/issuesecurityschemes/{id}` — Get issue security scheme

- Request: [[Jira v3 - Get issue security scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
