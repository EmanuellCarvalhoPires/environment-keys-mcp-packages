---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-statuses
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_status
title: "Jira v3 - Get status"
kind: request
request: "[[Jira v3 - Get status]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/status/{idOrName} · Get status. Returns a status. The status must be associated with an active workflow to be returned. If a name is used on more than one status, only the status found first is returned. Therefore, identifying the status by its ID may be preferable. This operation can be accessed anonymously. Writes data: no."
params:
  "idOrName":
    type: string
    required: true
    description: "The ID or name of the status."
writes: false
expose: false
---
# jira_get_status

`GET /rest/api/3/status/{idOrName}` — Get status

- Request: [[Jira v3 - Get status]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
