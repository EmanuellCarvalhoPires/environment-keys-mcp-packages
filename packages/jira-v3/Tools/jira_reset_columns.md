---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_reset_columns
title: "Jira v3 - Reset columns"
kind: request
request: "[[Jira v3 - Reset columns]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/filter/{id}/columns · Reset columns. Reset the user's column configuration for the filter to the default. Permissions required: Permission to access Jira, however, columns are only reset for: filters owned by the user. filters shared with a group that the user is a member of. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the filter."
writes: true
expose: false
---
# jira_reset_columns

`DELETE /rest/api/3/filter/{id}/columns` — Reset columns

- Request: [[Jira v3 - Reset columns]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
