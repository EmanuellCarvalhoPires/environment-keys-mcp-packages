---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-search
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_find_users_with_permissions
title: "Jira v3 - Find users with permissions"
kind: request
request: "[[Jira v3 - Find users with permissions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/user/permission/search · Find users with permissions. Returns a list of users who fulfill these criteria: their user attributes match a search string. they have a set of permissions for a project or issue. If no search string is provided, a list of all users with the permissions is returned. Writes data: no."
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
  "permissions":
    type: string
    required: true
    description: "A comma separated list of permissions. Permissions can be specified as any: permission returned by Get all permissions. custom project permission added by Connect apps."
  "issueKey":
    type: string
    required: false
    description: "The issue key for the issue."
  "projectKey":
    type: string
    required: false
    description: "The project key for the project (case sensitive)."
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
# jira_find_users_with_permissions

`GET /rest/api/3/user/permission/search` — Find users with permissions

- Request: [[Jira v3 - Find users with permissions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
