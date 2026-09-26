---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/users
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_bulk_get_users
title: "Jira v3 - Bulk get users"
kind: request
request: "[[Jira v3 - Bulk get users]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/user/bulk · Bulk get users. Returns a paginated list of the users specified by one or more account IDs. Permissions required: Permission to access Jira. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "username":
    type: string
    required: false
    description: "This parameter is no longer available and will be removed from the documentation soon. See the deprecation notice for details."
  "key":
    type: string
    required: false
    description: "This parameter is no longer available and will be removed from the documentation soon. See the deprecation notice for details."
  "accountId":
    type: string
    required: true
    description: "The account ID of a user. To specify multiple users, pass multiple accountId parameters. For example, accountId=5b10a2844c20165700ede21g&accountId=5b10ac8d82e05b22cc7d4ef5."
writes: false
expose: false
---
# jira_bulk_get_users

`GET /rest/api/3/user/bulk` — Bulk get users

- Request: [[Jira v3 - Bulk get users]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
