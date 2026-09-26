---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/avatars
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_avatars
title: "Jira v3 - Get avatars"
kind: request
request: "[[Jira v3 - Get avatars]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/universal_avatar/type/{type}/owner/{entityId} · Get avatars. Returns the system and custom avatars for a project, issue type or priority. This operation can be accessed anonymously. Permissions required: for custom project avatars, Browse projects project permission for the project the avatar belongs to. Writes data: no."
params:
  "type":
    type: string
    required: true
    description: "The avatar type."
  "entityId":
    type: string
    required: true
    description: "The ID of the item the avatar is associated with."
writes: false
expose: false
---
# jira_get_avatars

`GET /rest/api/3/universal_avatar/type/{type}/owner/{entityId}` — Get avatars

- Request: [[Jira v3 - Get avatars]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
