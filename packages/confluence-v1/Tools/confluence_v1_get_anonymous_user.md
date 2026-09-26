---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/users
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_anonymous_user
title: "Confluence v1 - Get anonymous user"
kind: request
request: "[[Confluence v1 - Get anonymous user]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/user/anonymous · Get anonymous user. Returns information about how anonymous users are represented, like the profile picture and display name. Permissions required: Permission to access the Confluence site ('Can use' global permission). Writes data: no."
params:
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the user to expand. - operations returns the operations that the user is allowed to do."
writes: false
expose: false
---
# confluence_v1_get_anonymous_user

`GET /wiki/rest/api/user/anonymous` — Get anonymous user

- Request: [[Confluence v1 - Get anonymous user]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
