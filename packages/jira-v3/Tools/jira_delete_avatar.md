---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/avatars
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_avatar
title: "Jira v3 - Delete avatar"
kind: request
request: "[[Jira v3 - Delete avatar]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id} · Delete avatar. Deletes an avatar from a project, issue type or priority. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "type":
    type: string
    required: true
    description: "The avatar type."
  "owningObjectId":
    type: string
    required: true
    description: "The ID of the item the avatar is associated with."
  "id":
    type: string
    required: true
    description: "The ID of the avatar."
writes: true
expose: false
---
# jira_delete_avatar

`DELETE /rest/api/3/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id}` — Delete avatar

- Request: [[Jira v3 - Delete avatar]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
