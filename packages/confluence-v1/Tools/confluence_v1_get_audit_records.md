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
tool: confluence_v1_get_audit_records
title: "Confluence v1 - Get audit records"
kind: request
request: "[[Confluence v1 - Get audit records]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/audit · Get audit records. Returns all records in the audit log, optionally for a certain date range. This contains information about events like space exports, group membership changes, app installations, etc. For more information, see Audit log in the Confluence administrator's guide. Writes data: no."
params:
  "startDate":
    type: string
    required: false
    description: "Filters the results to the records on or after the startDate. The startDate must be specified as epoch time in milliseconds."
  "endDate":
    type: string
    required: false
    description: "Filters the results to the records on or before the endDate. The endDate must be specified as epoch time in milliseconds."
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
# confluence_v1_get_audit_records

`GET /wiki/rest/api/audit` — Get audit records

- Request: [[Confluence v1 - Get audit records]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
