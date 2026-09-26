---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-priorities
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_priority
title: "Jira v3 - Get priority"
kind: request
request: "[[Jira v3 - Get priority]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/priority/{id} · Get priority. Returns an issue priority. To fetch multiple priorities at once, use Search priorities instead. Permissions required: Permission to access Jira. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the issue priority."
writes: false
expose: false
---
# jira_get_priority

`GET /rest/api/3/priority/{id}` — Get priority

- Request: [[Jira v3 - Get priority]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
