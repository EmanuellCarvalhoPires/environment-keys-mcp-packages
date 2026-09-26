---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_custom_field
title: "Jira v3 - Update custom field"
kind: request
request: "[[Jira v3 - Update custom field]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/field/{fieldId} · Update custom field. Updates a custom field. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the custom field."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_custom_field

`PUT /rest/api/3/field/{fieldId}` — Update custom field

- Request: [[Jira v3 - Update custom field]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
