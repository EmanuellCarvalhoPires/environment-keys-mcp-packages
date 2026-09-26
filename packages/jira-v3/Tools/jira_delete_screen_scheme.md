---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_screen_scheme
title: "Jira v3 - Delete screen scheme"
kind: request
request: "[[Jira v3 - Delete screen scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/screenscheme/{screenSchemeId} · Delete screen scheme. Deletes a screen scheme. A screen scheme cannot be deleted if it is used in an issue type screen scheme. Only screens schemes used in classic projects can be deleted. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "screenSchemeId":
    type: string
    required: true
    description: "The ID of the screen scheme."
writes: true
expose: false
---
# jira_delete_screen_scheme

`DELETE /rest/api/3/screenscheme/{screenSchemeId}` — Delete screen scheme

- Request: [[Jira v3 - Delete screen scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
