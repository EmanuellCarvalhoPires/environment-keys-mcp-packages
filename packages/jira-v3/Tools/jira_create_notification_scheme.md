---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-notification-schemes
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_notification_scheme
title: "Jira v3 - Create notification scheme"
kind: request
request: "[[Jira v3 - Create notification scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/notificationscheme · Create notification scheme. Creates a notification scheme with notifications. You can create up to 1000 notifications per request. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_notification_scheme

`POST /rest/api/3/notificationscheme` — Create notification scheme

- Request: [[Jira v3 - Create notification scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
