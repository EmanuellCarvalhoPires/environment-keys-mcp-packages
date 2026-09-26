---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-priorities
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_priority
title: "Jira v3 - Create priority"
kind: request
request: "[[Jira v3 - Create priority]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/priority · Create priority. Creates an issue priority. Deprecation notice: The iconUrl parameter was sunset on 16th Mar 2025, and replaced with avatarId. See CHANGE-1525. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_priority

`POST /rest/api/3/priority` — Create priority

- Request: [[Jira v3 - Create priority]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
