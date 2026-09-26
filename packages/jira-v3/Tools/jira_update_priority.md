---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-priorities
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_priority
title: "Jira v3 - Update priority"
kind: request
request: "[[Jira v3 - Update priority]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/priority/{id} · Update priority. Updates an issue priority. At least one request body parameter must be defined. Deprecation notice: The iconUrl parameter was sunset on 16th Mar 2025, and replaced with avatarId. See CHANGE-1525. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the issue priority."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_priority

`PUT /rest/api/3/priority/{id}` — Update priority

- Request: [[Jira v3 - Update priority]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
