---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/group-and-user-picker
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_find_users_and_groups
title: "Jira v3 - Find users and groups"
kind: request
request: "[[Jira v3 - Find users and groups]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/groupuserpicker · Find users and groups. Returns a list of users and groups matching a string. The string is used: for users, to find a case-insensitive match with display name and e-mail address. Writes data: no."
params:
  "query":
    type: string
    required: true
    description: "The search string."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return in each list."
  "showAvatar":
    type: string
    required: false
    description: "Whether the user avatar should be returned. If an invalid value is provided, the default value is used."
  "fieldId":
    type: string
    required: false
    description: "The custom field ID of the field this request is for."
  "projectId":
    type: string
    required: false
    description: "The ID of a project that returned users and groups must have permission to view. To include multiple projects, provide an ampersand-separated list. For example, projectId=10000&projectId=10001."
  "issueTypeId":
    type: string
    required: false
    description: "The ID of an issue type that returned users and groups must have permission to view. To include multiple issue types, provide an ampersand-separated list."
  "avatarSize":
    type: string
    required: false
    description: "The size of the avatar to return. If an invalid value is provided, the default value is used."
  "caseInsensitive":
    type: string
    required: false
    description: "Whether the search for groups should be case insensitive."
  "excludeConnectAddons":
    type: string
    required: false
    description: "Whether Connect app users and groups should be excluded from the search results. If an invalid value is provided, the default value is used."
  "includeAiAgents":
    type: string
    required: false
    description: "Whether AI Agents should be included in the search results. If an invalid value is provided, the default value is used."
writes: false
expose: false
---
# jira_find_users_and_groups

`GET /rest/api/3/groupuserpicker` — Find users and groups

- Request: [[Jira v3 - Find users and groups]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
