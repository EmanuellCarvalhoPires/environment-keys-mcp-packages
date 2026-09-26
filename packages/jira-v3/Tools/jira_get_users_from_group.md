---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/groups
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_users_from_group
title: "Jira v3 - Get users from group"
kind: request
request: "[[Jira v3 - Get users from group]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/group/member · Get users from group. Returns a paginated list of all users in a group. Note that users are ordered by username, however the username is not returned in the results due to privacy reasons. Permissions required: either of: Browse users and groups global permission. Administer Jira global permission. Writes data: no."
params:
  "groupname":
    type: string
    required: false
    description: "As a group's name can change, use of groupId is recommended to identify a group. The name of the group. This parameter cannot be used with the groupId parameter."
  "groupId":
    type: string
    required: false
    description: "The ID of the group. This parameter cannot be used with the groupName parameter."
  "includeInactiveUsers":
    type: string
    required: false
    description: "Include inactive users."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page (number should be between 1 and 50)."
writes: false
expose: false
---
# jira_get_users_from_group

`GET /rest/api/3/group/member` — Get users from group

- Request: [[Jira v3 - Get users from group]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
