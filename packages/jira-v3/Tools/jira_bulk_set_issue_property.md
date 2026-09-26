---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-properties
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_bulk_set_issue_property
title: "Jira v3 - Bulk set issue property"
kind: request
request: "[[Jira v3 - Bulk set issue property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issue/properties/{propertyKey} · Bulk set issue property. Sets a property value on multiple issues. The value set can be a constant or determined by a Jira expression. Expressions must be computable with constant complexity when applied to a set of issues. Writes data: yes."
params:
  "propertyKey":
    type: string
    required: true
    description: "The key of the property. The maximum length is 255 characters."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_set_issue_property

`PUT /rest/api/3/issue/properties/{propertyKey}` — Bulk set issue property

- Request: [[Jira v3 - Bulk set issue property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
