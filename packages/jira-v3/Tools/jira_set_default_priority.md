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
tool: jira_set_default_priority
title: "Jira v3 - Set default priority"
kind: request
request: "[[Jira v3 - Set default priority]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/priority/default · Set default priority. Sets default issue priority. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_default_priority

`PUT /rest/api/3/priority/default` — Set default priority

- Request: [[Jira v3 - Set default priority]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
