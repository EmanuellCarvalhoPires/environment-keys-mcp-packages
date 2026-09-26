---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/webhooks
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_webhooks_by_id
title: "Jira v3 - Delete webhooks by ID"
kind: request
request: "[[Jira v3 - Delete webhooks by ID]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/webhook · Delete webhooks by ID. Removes webhooks by ID. Only webhooks registered by the calling app are removed. If webhooks created by other apps are specified, they are ignored. Permissions required: Only Connect and OAuth 2.0 apps can use this operation. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_delete_webhooks_by_id

`DELETE /rest/api/3/webhook` — Delete webhooks by ID

- Request: [[Jira v3 - Delete webhooks by ID]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
