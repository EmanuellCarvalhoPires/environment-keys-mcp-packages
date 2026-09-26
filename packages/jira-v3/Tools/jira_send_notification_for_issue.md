---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_send_notification_for_issue
title: "Jira v3 - Send notification for issue"
kind: request
request: "[[Jira v3 - Send notification for issue]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issue/{issueIdOrKey}/notify · Send notification for issue. Creates an email notification for an issue and adds it to the mail queue. Permissions required: Browse Projects project permission for the project that the issue is in. If issue-level security is configured, issue-level security permission to view the issue. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "ID or key of the issue that the notification is sent for."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_send_notification_for_issue

`POST /rest/api/3/issue/{issueIdOrKey}/notify` — Send notification for issue

- Request: [[Jira v3 - Send notification for issue]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
