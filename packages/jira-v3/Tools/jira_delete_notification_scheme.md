---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-notification-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_notification_scheme
title: "Jira v3 - Delete notification scheme"
kind: request
request: "[[Jira v3 - Delete notification scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/notificationscheme/{notificationSchemeId} · Delete notification scheme. Deletes a notification scheme. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "notificationSchemeId":
    type: string
    required: true
    description: "The ID of the notification scheme."
writes: true
expose: false
---
# jira_delete_notification_scheme

`DELETE /rest/api/3/notificationscheme/{notificationSchemeId}` — Delete notification scheme

- Request: [[Jira v3 - Delete notification scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
