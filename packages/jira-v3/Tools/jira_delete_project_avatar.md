---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-avatars
  - api/operation/delete
  - api/effect/write
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_project_avatar
title: "Jira v3 - Delete project avatar"
kind: request
request: "[[Jira v3 - Delete project avatar]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/project/{projectIdOrKey}/avatar/{id} · Delete project avatar. Deletes a custom avatar from a project. Note that system avatars cannot be deleted. Permissions required: Administer projects project permission. Writes data: yes."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or (case-sensitive) key."
  "id":
    type: string
    required: true
    description: "The ID of the avatar."
writes: true
expose: false
---
# jira_delete_project_avatar

`DELETE /rest/api/3/project/{projectIdOrKey}/avatar/{id}` — Delete project avatar

- Request: [[Jira v3 - Delete project avatar]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
