---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/avatars
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_system_avatars_by_type
title: "Jira v3 - Get system avatars by type"
kind: request
request: "[[Jira v3 - Get system avatars by type]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/avatar/{type}/system · Get system avatars by type. Returns a list of system avatar details by owner type, where the owner types are issue type, project, user or priority. This operation can be accessed anonymously. Permissions required: None. Writes data: no."
params:
  "type":
    type: string
    required: true
    description: "The avatar type."
writes: false
expose: false
---
# jira_get_system_avatars_by_type

`GET /rest/api/3/avatar/{type}/system` — Get system avatars by type

- Request: [[Jira v3 - Get system avatars by type]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
