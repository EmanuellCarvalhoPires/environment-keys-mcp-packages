---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/license-metrics
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_approximate_license_count
title: "Jira v3 - Get approximate license count"
kind: request
request: "[[Jira v3 - Get approximate license count]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/license/approximateLicenseCount · Get approximate license count. Returns the approximate number of user accounts across all Jira licenses. Note that this information is cached with a 7-day lifecycle and could be stale at the time of call. Permissions required: Administer Jira global permission. Writes data: no."
writes: false
expose: false
---
# jira_get_approximate_license_count

`GET /rest/api/3/license/approximateLicenseCount` — Get approximate license count

- Request: [[Jira v3 - Get approximate license count]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
