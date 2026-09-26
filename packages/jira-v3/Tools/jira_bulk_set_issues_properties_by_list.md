---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-properties
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_bulk_set_issues_properties_by_list
title: "Jira v3 - Bulk set issues properties by list"
kind: request
request: "[[Jira v3 - Bulk set issues properties by list]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issue/properties · Bulk set issues properties by list. Sets or updates a list of entity property values on issues. A list of up to 10 entity properties can be specified along with up to 10,000 issues on which to set or update that list of entity properties. The value of the request body must be a valid, non-empty JSON. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_set_issues_properties_by_list

`POST /rest/api/3/issue/properties` — Bulk set issues properties by list

- Request: [[Jira v3 - Bulk set issues properties by list]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
