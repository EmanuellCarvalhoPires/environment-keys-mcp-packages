---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_adf_limit_report
title: "Jira v3 - Get issue adf limit report"
kind: request
request: "[[Jira v3 - Get issue adf limit report]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/limit/adf/report · Get issue adf limit report. Returns all issues whose ADF (rich text) field data breaches the universal ADF size limit. Unlike the issue limit report, which reports issues breaching per-issue entity count limits, this endpoint reports issues whose ADF field byte size exceeds that limit. Writes data: no."
params:
  "isReturningKeys":
    type: string
    required: false
    description: "Return issue keys instead of issue ids in the response. Usage: Add ?isReturningKeys=true to the end of the path to request issue keys."
  "fieldType":
    type: string
    required: false
    description: "Restrict the report to the given ADF field types. Defaults to every ADF field type. For sites with a high issue volume, consider requesting field types individually to avoid timeouts."
writes: false
expose: false
---
# jira_get_issue_adf_limit_report

`GET /rest/api/3/issue/limit/adf/report` — Get issue adf limit report

- Request: [[Jira v3 - Get issue adf limit report]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
