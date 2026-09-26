---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tab-fields
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_all_screen_tab_fields
title: "Jira v3 - Get all screen tab fields"
kind: request
request: "[[Jira v3 - Get all screen tab fields]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/screens/{screenId}/tabs/{tabId}/fields · Get all screen tab fields. Returns all fields for a screen tab. Permissions required: Administer Jira global permission. Administer projects project permission when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme. Writes data: no."
params:
  "screenId":
    type: string
    required: true
    description: "The ID of the screen."
  "tabId":
    type: string
    required: true
    description: "The ID of the screen tab."
  "projectKey":
    type: string
    required: false
    description: "The key of the project."
writes: false
expose: false
---
# jira_get_all_screen_tab_fields

`GET /rest/api/3/screens/{screenId}/tabs/{tabId}/fields` — Get all screen tab fields

- Request: [[Jira v3 - Get all screen tab fields]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
