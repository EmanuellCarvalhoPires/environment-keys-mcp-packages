---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/user
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_create_bulk_user_lookup_using_ids
title: "Confluence v2 - Create bulk user lookup using ids"
kind: request
request: "[[Confluence v2 - Create bulk user lookup using ids]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /users-bulk · Create bulk user lookup using ids. Returns user details for the ids provided in the request body. Permissions required: Permission to access the Confluence site ('Can use' global permission). The user must be able to view user profiles in the Confluence site. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_bulk_user_lookup_using_ids

`POST /users-bulk` — Create bulk user lookup using ids

- Request: [[Confluence v2 - Create bulk user lookup using ids]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
