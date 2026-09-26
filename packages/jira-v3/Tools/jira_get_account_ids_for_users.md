---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/users
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_account_ids_for_users
title: "Jira v3 - Get account IDs for users"
kind: request
request: "[[Jira v3 - Get account IDs for users]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/user/bulk/migration · Get account IDs for users. Returns the account IDs for the users specified in the key or username parameters. Note that multiple key or username parameters can be specified. Permissions required: Permission to access Jira. Writes data: no."
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
    description: "Username of a user. To specify multiple users, pass multiple copies of this parameter. For example, username=fred&username=barney. Required if key isn't provided. Cannot be provided if key is present."
  "key":
    type: string
    required: false
    description: "Key of a user. To specify multiple users, pass multiple copies of this parameter. For example, key=fred&key=barney. Required if username isn't provided. Cannot be provided if username is present."
writes: false
expose: false
---
# jira_get_account_ids_for_users

`GET /rest/api/3/user/bulk/migration` — Get account IDs for users

- Request: [[Jira v3 - Get account IDs for users]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
