---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_find_users_assignable_to_projects
title: "Jira v3 - Find users assignable to projects"
kind: request
request: "[[Jira v3 - Find users assignable to projects]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/user/assignable/multiProjectSearch · Find users assignable to projects. Returns a list of users who can be assigned issues in one or more projects. The list may be restricted to users whose attributes match a string. Writes data: no."
params:
  "query":
    type: string
    required: false
    description: "A query string that is matched against user attributes, such as displayName and emailAddress, to find relevant users. The string can match the prefix of the attribute's value."
  "username":
    type: string
    required: false
    description: "This parameter is no longer available. See the deprecation notice for details."
  "accountId":
    type: string
    required: false
    description: "A query string that is matched exactly against user accountId. Required, unless query is specified."
  "projectKeys":
    type: string
    required: true
    description: "A list of project keys (case sensitive). This parameter accepts a comma-separated list."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
writes: false
expose: false
---
# jira_find_users_assignable_to_projects

`GET /rest/api/3/user/assignable/multiProjectSearch` — Find users assignable to projects

- Request: [[Jira v3 - Find users assignable to projects]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
