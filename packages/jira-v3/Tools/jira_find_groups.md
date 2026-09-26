---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/groups
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_find_groups
title: "Jira v3 - Find groups"
kind: request
request: "[[Jira v3 - Find groups]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/groups/picker · Find groups. Returns a list of groups whose names contain a query string. A list of group names can be provided to exclude groups from the results. The primary use case for this resource is to populate a group picker suggestions list. Writes data: no."
params:
  "accountId":
    type: string
    required: false
    description: "This parameter is deprecated, setting it does not affect the results. To find groups containing a particular user, use Get user groups."
  "query":
    type: string
    required: false
    description: "The string to find in group names."
  "exclude":
    type: string
    required: false
    description: "As a group's name can change, use of excludeGroupIds is recommended to identify a group. A group to exclude from the result. To exclude multiple groups, provide an ampersand-separated list."
  "excludeId":
    type: string
    required: false
    description: "A group ID to exclude from the result. To exclude multiple groups, provide an ampersand-separated list. For example, excludeId=group1-id&excludeId=group2-id."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of groups to return. The maximum number of groups that can be returned is limited by the system property jira.ajax.autocomplete.limit."
  "caseInsensitive":
    type: string
    required: false
    description: "Whether the search for groups should be case insensitive."
  "userName":
    type: string
    required: false
    description: "This parameter is no longer available. See the deprecation notice for details."
writes: false
expose: false
---
# jira_find_groups

`GET /rest/api/3/groups/picker` — Find groups

- Request: [[Jira v3 - Find groups]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
