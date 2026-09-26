---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_find_users_assignable_to_issues
title: "Jira v3 - Find users assignable to issues"
kind: request
request: "[[Jira v3 - Find users assignable to issues]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/user/assignable/search · Find users assignable to issues. Returns a list of users that can be assigned to an issue. Use this operation to find the list of users who can be assigned to: a new issue, by providing the projectKeyOrId. an updated issue, by providing the issueKey or issueId. Writes data: no."
params:
  "query":
    type: string
    required: false
    description: "A query string that is matched against user attributes, such as displayName, and emailAddress, to find relevant users. The string can match the prefix of the attribute's value."
  "sessionId":
    type: string
    required: false
    description: "The sessionId of this request. SessionId is the same until the assignee is set."
  "username":
    type: string
    required: false
    description: "This parameter is no longer available. See the deprecation notice for details."
  "accountId":
    type: string
    required: false
    description: "A query string that is matched exactly against user accountId. Required, unless query is specified."
  "project":
    type: string
    required: false
    description: "The project ID or project key (case sensitive). Required, unless issueKey or issueId is specified."
  "issueKey":
    type: string
    required: false
    description: "The key of the issue. Required, unless issueId or project is specified."
  "issueId":
    type: string
    required: false
    description: "The ID of the issue. Required, unless issueKey or project is specified."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return. This operation may return less than the maximum number of items even if more are available."
  "actionDescriptorId":
    type: string
    required: false
    description: "The ID of the transition."
  "recommend":
    type: string
    required: false
    description: "Query parameter recommend."
  "accountType":
    type: string
    required: false
    description: "Query parameter accountType."
  "appType":
    type: string
    required: false
    description: "Query parameter appType."
writes: false
expose: false
---
# jira_find_users_assignable_to_issues

`GET /rest/api/3/user/assignable/search` — Find users assignable to issues

- Request: [[Jira v3 - Find users assignable to issues]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
