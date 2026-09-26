---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-types
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_issue_type
title: "Jira v3 - Create issue type"
kind: request
request: "[[Jira v3 - Create issue type]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issuetype · Create issue type. Creates an issue type. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_issue_type

`POST /rest/api/3/issuetype` — Create issue type

- Request: [[Jira v3 - Create issue type]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
