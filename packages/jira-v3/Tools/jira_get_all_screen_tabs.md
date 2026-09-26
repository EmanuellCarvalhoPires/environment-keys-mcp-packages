---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tabs
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_all_screen_tabs
title: "Jira v3 - Get all screen tabs"
kind: request
request: "[[Jira v3 - Get all screen tabs]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/screens/{screenId}/tabs · Get all screen tabs. Returns the list of tabs for a screen. Permissions required: Administer Jira global permission. Administer projects project permission when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme. Writes data: no."
params:
  "screenId":
    type: string
    required: true
    description: "The ID of the screen."
  "projectKey":
    type: string
    required: false
    description: "The key of the project."
writes: false
expose: false
---
# jira_get_all_screen_tabs

`GET /rest/api/3/screens/{screenId}/tabs` — Get all screen tabs

- Request: [[Jira v3 - Get all screen tabs]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
