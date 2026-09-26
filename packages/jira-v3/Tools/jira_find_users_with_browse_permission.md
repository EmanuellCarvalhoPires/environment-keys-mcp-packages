---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_find_users_with_browse_permission
title: "Jira v3 - Find users with browse permission"
kind: request
request: "[[Jira v3 - Find users with browse permission]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/user/viewissue/search · Find users with browse permission. Returns a list of users who fulfill these criteria: their user attributes match a search string. they have permission to browse issues. Use this resource to find users who can browse: an issue, by providing the issueKey. any issue in a project, by providing the projectKey. Writes data: no."
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
  "issueKey":
    type: string
    required: false
    description: "The issue key for the issue. Required, unless projectKey is specified."
  "projectKey":
    type: string
    required: false
    description: "The project key for the project (case sensitive). Required, unless issueKey is specified."
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
# jira_find_users_with_browse_permission

`GET /rest/api/3/user/viewissue/search` — Find users with browse permission

- Request: [[Jira v3 - Find users with browse permission]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
