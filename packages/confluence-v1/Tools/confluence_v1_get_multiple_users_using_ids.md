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
tool: confluence_v1_get_multiple_users_using_ids
title: "Confluence v1 - Get multiple users using ids"
kind: request
request: "[[Confluence v1 - Get multiple users using ids]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/user/bulk · Get multiple users using ids. Returns user details for the ids provided in the request. Currently this API returns a maximum of 100 results. If more than 100 account ids are passed in, then the first 100 will be returned. Writes data: no."
params:
  "accountId":
    type: string
    required: true
    description: "A list of accountId's of users to be returned."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the user to expand. - operations returns the operations that the user is allowed to do."
writes: false
expose: false
---
# confluence_v1_get_multiple_users_using_ids

`GET /wiki/rest/api/user/bulk` — Get multiple users using ids

- Request: [[Confluence v1 - Get multiple users using ids]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
