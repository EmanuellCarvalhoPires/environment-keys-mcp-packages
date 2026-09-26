---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_filter
title: "Jira v3 - Delete filter"
kind: request
request: "[[Jira v3 - Delete filter]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/filter/{id} · Delete filter. Delete a filter. Permissions required: Permission to access Jira, however filters can only be deleted by the creator of the filter or a user with Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the filter to delete."
writes: true
expose: false
---
# jira_delete_filter

`DELETE /rest/api/3/filter/{id}` — Delete filter

- Request: [[Jira v3 - Delete filter]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
