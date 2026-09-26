---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/license-metrics
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_license
title: "Jira v3 - Get license"
kind: request
request: "[[Jira v3 - Get license]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/instance/license · Get license. Returns licensing information about the Jira instance. Permissions required: None. Writes data: no."
writes: false
expose: false
---
# jira_get_license

`GET /rest/api/3/instance/license` — Get license

- Request: [[Jira v3 - Get license]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
