---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-components
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_component
title: "Jira v3 - Get component"
kind: request
request: "[[Jira v3 - Get component]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/component/{id} · Get component. Returns a component. This operation can be accessed anonymously. Permissions required: Browse projects project permission for project containing the component. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the component."
writes: false
expose: false
---
# jira_get_component

`GET /rest/api/3/component/{id}` — Get component

- Request: [[Jira v3 - Get component]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
