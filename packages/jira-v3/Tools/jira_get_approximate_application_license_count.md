---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/license-metrics
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_approximate_application_license_count
title: "Jira v3 - Get approximate application license count"
kind: request
request: "[[Jira v3 - Get approximate application license count]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/license/approximateLicenseCount/product/{applicationKey} · Get approximate application license count. Returns the total approximate number of user accounts for a single Jira license. Note that this information is cached with a 7-day lifecycle and could be stale at the time of call. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "applicationKey":
    type: string
    required: true
    description: "The ID of the application, represents a specific version of Jira."
writes: false
expose: false
---
# jira_get_approximate_application_license_count

`GET /rest/api/3/license/approximateLicenseCount/product/{applicationKey}` — Get approximate application license count

- Request: [[Jira v3 - Get approximate application license count]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
