---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filter-sharing
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_share_permissions
title: "Jira v3 - Get share permissions"
kind: request
request: "[[Jira v3 - Get share permissions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/filter/{id}/permission · Get share permissions. Returns the share permissions for a filter. A filter can be shared with groups, projects, all logged-in users, or the public. Sharing with all logged-in users or the public is known as a global share permission. This operation can be accessed anonymously. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the filter."
writes: false
expose: false
---
# jira_get_share_permissions

`GET /rest/api/3/filter/{id}/permission` — Get share permissions

- Request: [[Jira v3 - Get share permissions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
