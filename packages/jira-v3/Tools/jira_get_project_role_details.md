---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-roles
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_project_role_details
title: "Jira v3 - Get project role details"
kind: request
request: "[[Jira v3 - Get project role details]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectIdOrKey}/roledetails · Get project role details. Returns all project roles and the details for each role. Note that the list of project roles is common to all projects. This operation can be accessed anonymously. Permissions required: Administer Jira global permission or Administer projects project permission for the project. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
  "currentMember":
    type: string
    required: false
    description: "Whether the roles should be filtered to include only those the user is assigned to."
  "excludeConnectAddons":
    type: string
    required: false
    description: "Query parameter excludeConnectAddons."
  "excludeOtherServiceRoles":
    type: string
    required: false
    description: "Do not return the default JSM company-managed space from CSM spaces, or the default CSM roles from JSM spaces."
writes: false
expose: false
---
# jira_get_project_role_details

`GET /rest/api/3/project/{projectIdOrKey}/roledetails` — Get project role details

- Request: [[Jira v3 - Get project role details]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
