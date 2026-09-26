---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-level
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_security_level
title: "Jira v3 - Get issue security level"
kind: request
request: "[[Jira v3 - Get issue security level]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/securitylevel/{id} · Get issue security level. Returns details of an issue security level. Use Get issue security scheme to obtain the IDs of issue security levels associated with the issue security scheme. This operation can be accessed anonymously. Permissions required: None. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the issue security level."
writes: false
expose: false
---
# jira_get_issue_security_level

`GET /rest/api/3/securitylevel/{id}` — Get issue security level

- Request: [[Jira v3 - Get issue security level]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
