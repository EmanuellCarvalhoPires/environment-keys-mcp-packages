---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_dashboard
title: "Jira v3 - Delete dashboard"
kind: request
request: "[[Jira v3 - Delete dashboard]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/dashboard/{id} · Delete dashboard. Deletes a dashboard. Permissions required: None The dashboard to be deleted must be owned by the user. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the dashboard."
writes: true
expose: false
---
# jira_delete_dashboard

`DELETE /rest/api/3/dashboard/{id}` — Delete dashboard

- Request: [[Jira v3 - Delete dashboard]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
