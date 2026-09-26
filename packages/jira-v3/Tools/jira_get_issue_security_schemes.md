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
tool: jira_get_issue_security_schemes
title: "Jira v3 - Get issue security schemes"
kind: request
request: "[[Jira v3 - Get issue security schemes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuesecurityschemes · Get issue security schemes. Returns all issue security schemes. Permissions required: Administer Jira global permission. Writes data: no."
writes: false
expose: false
---
# jira_get_issue_security_schemes

`GET /rest/api/3/issuesecurityschemes` — Get issue security schemes

- Request: [[Jira v3 - Get issue security schemes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
