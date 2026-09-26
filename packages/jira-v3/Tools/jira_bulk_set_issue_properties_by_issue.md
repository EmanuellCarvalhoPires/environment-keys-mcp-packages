---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-properties
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_bulk_set_issue_properties_by_issue
title: "Jira v3 - Bulk set issue properties by issue"
kind: request
request: "[[Jira v3 - Bulk set issue properties by issue]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issue/properties/multi · Bulk set issue properties by issue. Sets or updates entity property values on issues. Up to 10 entity properties can be specified for each issue and up to 100 issues included in the request. The value of the request body must be a valid, non-empty JSON. This operation is: asynchronous. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_set_issue_properties_by_issue

`POST /rest/api/3/issue/properties/multi` — Bulk set issue properties by issue

- Request: [[Jira v3 - Bulk set issue properties by issue]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
