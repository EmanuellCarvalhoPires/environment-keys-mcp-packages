---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-templates
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_custom_project
title: "Jira v3 - Create custom project"
kind: request
request: "[[Jira v3 - Create custom project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/project-template · Create custom project. Creates a project based on a custom template provided in the request. The request body should contain the project details and the capabilities that comprise the project: details \\- represents the project details settings template \\- represents a list of capabilities responsible f… Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_custom_project

`POST /rest/api/3/project-template` — Create custom project

- Request: [[Jira v3 - Create custom project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
