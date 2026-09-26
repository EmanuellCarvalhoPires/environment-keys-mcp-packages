---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/audit-records
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_audit_records
title: "Jira v3 - Get audit records"
kind: request
request: "[[Jira v3 - Get audit records]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/auditing/record · Get audit records. Returns a list of audit records. The list can be filtered to include items: where each item in filter has at least one match in any of these fields: summary category eventSource objectItem.name If the object is a user, account ID is available to filter. Writes data: no."
params:
  "offset":
    type: string
    required: false
    description: "The number of records to skip before returning the first result."
  "limit":
    type: string
    required: false
    description: "The maximum number of results to return."
  "filter":
    type: string
    required: false
    description: "The strings to match with audit field content, space separated."
  "from":
    type: string
    required: false
    description: "The date and time on or after which returned audit records must have been created. If to is provided from must be before to or no audit records are returned."
  "to":
    type: string
    required: false
    description: "The date and time on or before which returned audit results must have been created. If from is provided to must be after from or no audit records are returned."
writes: false
expose: false
---
# jira_get_audit_records

`GET /rest/api/3/auditing/record` — Get audit records

- Request: [[Jira v3 - Get audit records]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
