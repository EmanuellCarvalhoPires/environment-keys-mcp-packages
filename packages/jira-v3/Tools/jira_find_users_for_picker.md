---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_find_users_for_picker
title: "Jira v3 - Find users for picker"
kind: request
request: "[[Jira v3 - Find users for picker]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/user/picker · Find users for picker. Returns a list of users whose attributes match the query term. The returned object includes the html field where the matched query term is highlighted with the HTML strong tag. A list of account IDs can be provided to exclude users from the results. Writes data: no."
params:
  "query":
    type: string
    required: true
    description: "A query string that is matched against user attributes, such as displayName, and emailAddress, to find relevant users. The string can match the prefix of the attribute's value."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return. The total number of matched users is returned in total."
  "showAvatar":
    type: string
    required: false
    description: "Include the URI to the user's avatar."
  "exclude":
    type: string
    required: false
    description: "This parameter is no longer available. See the deprecation notice for details."
  "excludeAccountIds":
    type: string
    required: false
    description: "A list of account IDs to exclude from the search results. This parameter accepts a comma-separated list. Multiple account IDs can also be provided using an ampersand-separated list."
  "avatarSize":
    type: string
    required: false
    description: "Query parameter avatarSize."
  "excludeConnectUsers":
    type: string
    required: false
    description: "Query parameter excludeConnectUsers."
writes: false
expose: false
---
# jira_find_users_for_picker

`GET /rest/api/3/user/picker` — Find users for picker

- Request: [[Jira v3 - Find users for picker]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
