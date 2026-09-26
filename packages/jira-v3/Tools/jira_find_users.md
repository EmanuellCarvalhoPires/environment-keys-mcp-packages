---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_find_users
title: "Jira v3 - Find users"
kind: request
request: "[[Jira v3 - Find users]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/user/search · Find users. Returns a list of active users that match the search string and property. This operation first applies a filter to match the search string and property, and then takes the filtered users in the range defined by startAt and maxResults, up to the thousandth user. Writes data: no."
params:
  "query":
    type: string
    required: false
    description: "A query string that is matched against user attributes ( displayName, and emailAddress) to find relevant users. The string can match the prefix of the attribute's value."
  "username":
    type: string
    required: false
    description: "Query parameter username."
  "accountId":
    type: string
    required: false
    description: "A query string that is matched exactly against a user accountId. Required, unless query or property is specified."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of filtered results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "property":
    type: string
    required: false
    description: "A query string used to search properties. Property keys are specified by path, so property keys containing dot (.) or equals (=) characters cannot be used."
writes: false
expose: true
---
# jira_find_users

`GET /rest/api/3/user/search` — Find users

- Request: [[Jira v3 - Find users]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
