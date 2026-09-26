---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_project
title: "Jira v3 - Create project"
kind: request
request: "[[Jira v3 - Create project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/project · Create project. Creates a project based on a project type template, as shown in the following table: | Project Type Key | Project Template Key | |--|--| | business | com.atlassian.jira-core-project-templates:jira-core-simplified-content-management, com.atlassian.jira-core-project-templates:jira-… Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_project

`POST /rest/api/3/project` — Create project

- Request: [[Jira v3 - Create project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
