---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-components
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_component
title: "Jira v3 - Update component"
kind: request
request: "[[Jira v3 - Update component]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/component/{id} · Update component. Updates a component. Any fields included in the request are overwritten. If leadAccountId is an empty string (\"\") the component lead is removed. This operation can be accessed anonymously. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the component."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_component

`PUT /rest/api/3/component/{id}` — Update component

- Request: [[Jira v3 - Update component]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
