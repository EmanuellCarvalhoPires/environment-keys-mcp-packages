---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-avatars
  - api/operation/update
  - api/effect/write
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_set_project_avatar
title: "Jira v3 - Set project avatar"
kind: request
request: "[[Jira v3 - Set project avatar]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/project/{projectIdOrKey}/avatar · Set project avatar. Sets the avatar displayed for a project. Use Load project avatar to store avatars against the project, before using this operation to set the displayed avatar. Permissions required: Administer projects project permission. Writes data: yes."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The ID or (case-sensitive) key of the project."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_project_avatar

`PUT /rest/api/3/project/{projectIdOrKey}/avatar` — Set project avatar

- Request: [[Jira v3 - Set project avatar]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
