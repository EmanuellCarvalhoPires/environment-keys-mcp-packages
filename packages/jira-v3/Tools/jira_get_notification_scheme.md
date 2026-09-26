---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-notification-schemes
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_notification_scheme
title: "Jira v3 - Get notification scheme"
kind: request
request: "[[Jira v3 - Get notification scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/notificationscheme/{id} · Get notification scheme. Returns a notification scheme, including the list of events and the recipients who will receive notifications for those events. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the notification scheme. Use Get notification schemes paginated to get a list of notification scheme IDs."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list."
writes: false
expose: false
---
# jira_get_notification_scheme

`GET /rest/api/3/notificationscheme/{id}` — Get notification scheme

- Request: [[Jira v3 - Get notification scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
