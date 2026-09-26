---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/avatars
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_avatar_image_by_owner
title: "Jira v3 - Get avatar image by owner"
kind: request
request: "[[Jira v3 - Get avatar image by owner]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/universal_avatar/view/type/{type}/owner/{entityId} · Get avatar image by owner. Returns the avatar image for a project, issue type or priority. This operation can be accessed anonymously. Permissions required: For system avatars, none. For custom project avatars, Browse projects project permission for the project the avatar belongs to. Writes data: no."
params:
  "type":
    type: string
    required: true
    description: "The icon type of the avatar."
  "entityId":
    type: string
    required: true
    description: "The ID of the project or issue type the avatar belongs to."
  "size":
    type: string
    required: false
    description: "The size of the avatar image. If not provided the default size is returned."
  "format":
    type: string
    required: false
    description: "The format to return the avatar image in. If not provided the original content format is returned."
writes: false
expose: false
---
# jira_get_avatar_image_by_owner

`GET /rest/api/3/universal_avatar/view/type/{type}/owner/{entityId}` — Get avatar image by owner

- Request: [[Jira v3 - Get avatar image by owner]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
