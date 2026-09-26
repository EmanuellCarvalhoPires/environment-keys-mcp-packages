---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/avatars
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_avatar_image_by_type
title: "Jira v3 - Get avatar image by type"
kind: request
request: "[[Jira v3 - Get avatar image by type]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/universal_avatar/view/type/{type} · Get avatar image by type. Returns the default project, issue type or priority avatar image. This operation can be accessed anonymously. Permissions required: None. Writes data: no."
params:
  "type":
    type: string
    required: true
    description: "The icon type of the avatar."
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
# jira_get_avatar_image_by_type

`GET /rest/api/3/universal_avatar/view/type/{type}` — Get avatar image by type

- Request: [[Jira v3 - Get avatar image by type]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
