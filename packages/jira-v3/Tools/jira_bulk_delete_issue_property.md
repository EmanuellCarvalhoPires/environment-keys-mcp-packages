---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-properties
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_bulk_delete_issue_property
title: "Jira v3 - Bulk delete issue property"
kind: request
request: "[[Jira v3 - Bulk delete issue property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issue/properties/{propertyKey} · Bulk delete issue property. Deletes a property value from multiple issues. The issues to be updated can be specified by filter criteria. The criteria the filter used to identify eligible issues are: entityIds Only issues from this list are eligible. Writes data: yes."
params:
  "propertyKey":
    type: string
    required: true
    description: "The key of the property."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_bulk_delete_issue_property

`DELETE /rest/api/3/issue/properties/{propertyKey}` — Bulk delete issue property

- Request: [[Jira v3 - Bulk delete issue property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
