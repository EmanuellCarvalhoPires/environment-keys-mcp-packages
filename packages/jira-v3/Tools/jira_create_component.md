---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-components
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_component
title: "Jira v3 - Create component"
kind: request
request: "[[Jira v3 - Create component]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/component · Create component. Creates a component. Use components to provide containers for issues within a project. Use components to provide containers for issues within a project. This operation can be accessed anonymously. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_component

`POST /rest/api/3/component` — Create component

- Request: [[Jira v3 - Create component]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
