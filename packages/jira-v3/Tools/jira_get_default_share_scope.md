---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filter-sharing
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_default_share_scope
title: "Jira v3 - Get default share scope"
kind: request
request: "[[Jira v3 - Get default share scope]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/filter/defaultShareScope · Get default share scope. Returns the default sharing settings for new filters and dashboards for a user. Permissions required: Permission to access Jira. Writes data: no."
writes: false
expose: false
---
# jira_get_default_share_scope

`GET /rest/api/3/filter/defaultShareScope` — Get default share scope

- Request: [[Jira v3 - Get default share scope]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
