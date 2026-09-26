---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-avatars
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_all_project_avatars
title: "Jira v3 - Get all project avatars"
kind: request
request: "[[Jira v3 - Get all project avatars]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectIdOrKey}/avatars · Get all project avatars. Returns all project avatars, grouped by system and custom avatars. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The ID or (case-sensitive) key of the project."
writes: false
expose: false
---
# jira_get_all_project_avatars

`GET /rest/api/3/project/{projectIdOrKey}/avatars` — Get all project avatars

- Request: [[Jira v3 - Get all project avatars]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
