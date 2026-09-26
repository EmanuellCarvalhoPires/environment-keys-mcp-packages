---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_version
title: "Jira v3 - Create version"
kind: request
request: "[[Jira v3 - Create version]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/version · Create version. Creates a project version. This operation can be accessed anonymously. Permissions required: Administer Jira global permission or Administer Projects project permission for the project the version is added to. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_version

`POST /rest/api/3/version` — Create version

- Request: [[Jira v3 - Create version]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
