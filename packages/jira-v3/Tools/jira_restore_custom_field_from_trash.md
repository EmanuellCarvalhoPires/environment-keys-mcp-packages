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
tool: jira_restore_custom_field_from_trash
title: "Jira v3 - Restore custom field from trash"
kind: request
request: "[[Jira v3 - Restore custom field from trash]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/field/{id}/restore · Restore custom field from trash. Restores a custom field from trash. See Edit or delete a custom field for more information on trashing and deleting custom fields. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of a custom field."
writes: true
expose: false
---
# jira_restore_custom_field_from_trash

`POST /rest/api/3/field/{id}/restore` — Restore custom field from trash

- Request: [[Jira v3 - Restore custom field from trash]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
