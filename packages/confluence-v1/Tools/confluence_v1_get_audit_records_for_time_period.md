---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/audit
  - api/operation/list
  - api/effect/read
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_audit_records_for_time_period
title: "Confluence v1 - Get audit records for time period"
kind: request
request: "[[Confluence v1 - Get audit records for time period]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/audit/since · Get audit records for time period. Returns records from the audit log, for a time period back from the current date. For example, you can use this method to get the last 3 months of records. This contains information about events like space exports, group membership changes, app installations, etc. Writes data: no."
params:
  "number":
    type: string
    required: false
    description: "The number of units for the time period."
  "units":
    type: string
    required: false
    description: "The unit of time that the time period is measured in."
  "searchString":
    type: string
    required: false
    description: "Filters the results to records that have string property values matching the searchString."
  "start":
    type: string
    required: false
    description: "The starting index of the returned records."
  "limit":
    type: string
    required: false
    description: "The maximum number of records to return per page. Note, this may be restricted by fixed system limits."
writes: false
expose: false
---
# confluence_v1_get_audit_records_for_time_period

`GET /wiki/rest/api/audit/since` — Get audit records for time period

- Request: [[Confluence v1 - Get audit records for time period]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
