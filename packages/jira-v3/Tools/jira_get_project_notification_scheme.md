---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_project_notification_scheme
title: "Jira v3 - Get project notification scheme"
kind: request
request: "[[Jira v3 - Get project notification scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectKeyOrId}/notificationscheme · Get project notification scheme. Gets a notification scheme associated with the project. Permissions required: Administer Jira global permission or Administer Projects project permission. Writes data: no."
params:
  "projectKeyOrId":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list."
writes: false
expose: false
---
# jira_get_project_notification_scheme

`GET /rest/api/3/project/{projectKeyOrId}/notificationscheme` — Get project notification scheme

- Request: [[Jira v3 - Get project notification scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
