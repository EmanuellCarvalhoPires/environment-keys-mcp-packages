---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-permission-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_assign_permission_scheme
title: "Jira v3 - Assign permission scheme"
kind: request
request: "[[Jira v3 - Assign permission scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/project/{projectKeyOrId}/permissionscheme · Assign permission scheme. Assigns a permission scheme with a project. See Managing project permissions for more information about permission schemes. Permissions required: Administer Jira global permission Writes data: yes."
params:
  "projectKeyOrId":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_assign_permission_scheme

`PUT /rest/api/3/project/{projectKeyOrId}/permissionscheme` — Assign permission scheme

- Request: [[Jira v3 - Assign permission scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
