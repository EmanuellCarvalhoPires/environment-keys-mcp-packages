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
tool: confluence_v1_get_group_memberships_for_user
title: "Confluence v1 - Get group memberships for user"
kind: request
request: "[[Confluence v1 - Get group memberships for user]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/user/memberof · Get group memberships for user. Returns the groups that a user is a member of. Permissions required: Permission to access the Confluence site ('Can use' global permission). Writes data: no."
params:
  "accountId":
    type: string
    required: true
    description: "The account ID of the user. The accountId uniquely identifies the user across all Atlassian products. For example, 384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192."
  "start":
    type: string
    required: false
    description: "The starting index of the returned groups."
  "limit":
    type: string
    required: false
    description: "The maximum number of groups to return per page. Note, this may be restricted by fixed system limits."
writes: false
expose: false
---
# confluence_v1_get_group_memberships_for_user

`GET /wiki/rest/api/user/memberof` — Get group memberships for user

- Request: [[Confluence v1 - Get group memberships for user]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
