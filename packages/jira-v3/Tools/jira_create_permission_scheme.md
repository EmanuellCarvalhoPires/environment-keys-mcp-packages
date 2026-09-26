---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/permission-schemes
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_permission_scheme
title: "Jira v3 - Create permission scheme"
kind: request
request: "[[Jira v3 - Create permission scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/permissionscheme · Create permission scheme. Creates a new permission scheme. You can create a permission scheme with or without defining a set of permission grants. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_permission_scheme

`POST /rest/api/3/permissionscheme` — Create permission scheme

- Request: [[Jira v3 - Create permission scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
