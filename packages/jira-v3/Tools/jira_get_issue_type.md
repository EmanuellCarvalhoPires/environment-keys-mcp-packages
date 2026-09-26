---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-types
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_type
title: "Jira v3 - Get issue type"
kind: request
request: "[[Jira v3 - Get issue type]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuetype/{id} · Get issue type. Returns an issue type. This operation can be accessed anonymously. Permissions required: Browse projects project permission in a project the issue type is associated with or Administer Jira global permission. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the issue type."
writes: false
expose: false
---
# jira_get_issue_type

`GET /rest/api/3/issuetype/{id}` — Get issue type

- Request: [[Jira v3 - Get issue type]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
