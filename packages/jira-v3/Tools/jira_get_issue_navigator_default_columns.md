---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-navigator-settings
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_navigator_default_columns
title: "Jira v3 - Get issue navigator default columns"
kind: request
request: "[[Jira v3 - Get issue navigator default columns]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/settings/columns · Get issue navigator default columns. Returns the default issue navigator columns. Permissions required: Administer Jira global permission. Writes data: no."
writes: false
expose: false
---
# jira_get_issue_navigator_default_columns

`GET /rest/api/3/settings/columns` — Get issue navigator default columns

- Request: [[Jira v3 - Get issue navigator default columns]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
