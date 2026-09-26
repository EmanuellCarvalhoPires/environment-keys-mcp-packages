---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_custom_field
title: "Jira v3 - Delete custom field"
kind: request
request: "[[Jira v3 - Delete custom field]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/field/{id} · Delete custom field. Deletes a custom field. The custom field is deleted whether it is in the trash or not. See Edit or delete a custom field for more information on trashing and deleting custom fields. This operation is asynchronous. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of a custom field."
writes: true
expose: false
---
# jira_delete_custom_field

`DELETE /rest/api/3/field/{id}` — Delete custom field

- Request: [[Jira v3 - Delete custom field]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
