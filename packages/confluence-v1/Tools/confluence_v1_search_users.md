---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/search
  - api/operation/search
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_search_users
title: "Confluence v1 - Search users"
kind: request
request: "[[Confluence v1 - Search users]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/search/user · Search users. Searches for users using user-specific queries from the Confluence Query Language (CQL). Note that CQL input queries submitted through the /wiki/rest/api/search/user endpoint only support user-specific fields like user, user.fullname, user.accountid, and user.userkey. Writes data: no."
params:
  "cql":
    type: string
    required: true
    description: "The CQL query to be used for the search. See Advanced Searching using CQL for instructions on how to build a CQL query."
  "start":
    type: string
    required: false
    description: "The starting index of the returned users."
  "limit":
    type: string
    required: false
    description: "The maximum number of user objects to return per page. Note, this may be restricted by fixed system limits."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the user to expand. - operations returns the operations for the user, which are used when setting permissions."
  "sitePermissionTypeFilter":
    type: string
    required: false
    description: "Filters users by permission type. Use none to default to licensed users, externalCollaborator for external/guest users, and all to include all permission types."
writes: false
expose: false
---
# confluence_v1_search_users

`GET /wiki/rest/api/search/user` — Search users

- Request: [[Confluence v1 - Search users]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
