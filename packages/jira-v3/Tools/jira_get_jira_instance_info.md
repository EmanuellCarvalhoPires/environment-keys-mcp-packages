---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/server-info
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_jira_instance_info
title: "Jira v3 - Get Jira instance info"
kind: request
request: "[[Jira v3 - Get Jira instance info]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/serverInfo · Get Jira instance info. Returns information about the Jira instance. This operation can be accessed anonymously. Permissions required: None. Writes data: no."
writes: false
expose: false
---
# jira_get_jira_instance_info

`GET /rest/api/3/serverInfo` — Get Jira instance info

- Request: [[Jira v3 - Get Jira instance info]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
