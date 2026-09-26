---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_move_custom_field_to_trash
title: "Jira v3 - Move custom field to trash"
kind: request
request: "[[Jira v3 - Move custom field to trash]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/field/{id}/trash · Move custom field to trash. Moves a custom field to trash. See Edit or delete a custom field for more information on trashing and deleting custom fields. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of a custom field."
writes: true
expose: false
---
# jira_move_custom_field_to_trash

`POST /rest/api/3/field/{id}/trash` — Move custom field to trash

- Request: [[Jira v3 - Move custom field to trash]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
