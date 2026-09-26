---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-permission-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_assigned_permission_scheme
title: "Jira v3 - Get assigned permission scheme"
kind: request
request: "[[Jira v3 - Get assigned permission scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectKeyOrId}/permissionscheme · Get assigned permission scheme. Gets the permission scheme associated with the project. Permissions required: Administer Jira global permission or Administer projects project permission. Writes data: no."
params:
  "projectKeyOrId":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value."
writes: false
expose: false
---
# jira_get_assigned_permission_scheme

`GET /rest/api/3/project/{projectKeyOrId}/permissionscheme` — Get assigned permission scheme

- Request: [[Jira v3 - Get assigned permission scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
