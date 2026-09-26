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
tool: jira_remove_notification_from_notification_scheme
title: "Jira v3 - Remove notification from notification scheme"
kind: request
request: "[[Jira v3 - Remove notification from notification scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/notificationscheme/{notificationSchemeId}/notification/{notificationId} · Remove notification from notification scheme. Removes a notification from a notification scheme. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "notificationSchemeId":
    type: string
    required: true
    description: "The ID of the notification scheme."
  "notificationId":
    type: string
    required: true
    description: "The ID of the notification."
writes: true
expose: false
---
# jira_remove_notification_from_notification_scheme

`DELETE /rest/api/3/notificationscheme/{notificationSchemeId}/notification/{notificationId}` — Remove notification from notification scheme

- Request: [[Jira v3 - Remove notification from notification scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
