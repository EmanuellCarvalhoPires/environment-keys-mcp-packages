---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-resolutions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_resolutions
title: "Jira v3 - Get resolutions"
kind: request
request: "[[Jira v3 - Get resolutions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/resolution · Get resolutions. Returns a list of all issue resolution values. Permissions required: Permission to access Jira. Writes data: no."
writes: false
expose: false
---
# jira_get_resolutions

`GET /rest/api/3/resolution` — Get resolutions

- Request: [[Jira v3 - Get resolutions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
