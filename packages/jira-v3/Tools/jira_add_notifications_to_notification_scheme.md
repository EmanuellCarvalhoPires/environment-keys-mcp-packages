---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-notification-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_add_notifications_to_notification_scheme
title: "Jira v3 - Add notifications to notification scheme"
kind: request
request: "[[Jira v3 - Add notifications to notification scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/notificationscheme/{id}/notification · Add notifications to notification scheme. Adds notifications to a notification scheme. You can add up to 1000 notifications per request. Deprecated: The notification type EmailAddress is no longer supported in Cloud. Refer to the changelog for more details. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the notification scheme."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_add_notifications_to_notification_scheme

`PUT /rest/api/3/notificationscheme/{id}/notification` — Add notifications to notification scheme

- Request: [[Jira v3 - Add notifications to notification scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
