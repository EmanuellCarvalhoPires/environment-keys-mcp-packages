---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-types
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_issue_type
title: "Jira v3 - Update issue type"
kind: request
request: "[[Jira v3 - Update issue type]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issuetype/{id} · Update issue type. Updates the issue type. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the issue type."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_issue_type

`PUT /rest/api/3/issuetype/{id}` — Update issue type

- Request: [[Jira v3 - Update issue type]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
