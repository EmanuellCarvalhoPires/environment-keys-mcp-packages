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
tool: jira_create_permission_grant
title: "Jira v3 - Create permission grant"
kind: request
request: "[[Jira v3 - Create permission grant]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/permissionscheme/{schemeId}/permission · Create permission grant. Creates a permission grant in a permission scheme. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "schemeId":
    type: string
    required: true
    description: "The ID of the permission scheme in which to create a new permission grant."
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
# jira_create_permission_grant

`POST /rest/api/3/permissionscheme/{schemeId}/permission` — Create permission grant

- Request: [[Jira v3 - Create permission grant]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
