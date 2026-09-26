---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/groups
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_bulk_get_groups
title: "Jira v3 - Bulk get groups"
kind: request
request: "[[Jira v3 - Bulk get groups]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/group/bulk · Bulk get groups. Returns a paginated list of groups. Permissions required: Browse users and groups global permission. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "groupId":
    type: string
    required: false
    description: "The ID of a group. To specify multiple IDs, pass multiple groupId parameters. For example, groupId=5b10a2844c20165700ede21g&groupId=5b10ac8d82e05b22cc7d4ef5."
  "groupName":
    type: string
    required: false
    description: "The name of a group. To specify multiple names, pass multiple groupName parameters. For example, groupName=administrators&groupName=jira-software-users."
  "accessType":
    type: string
    required: false
    description: "The access level of a group. Valid values: 'site-admin', 'admin', 'user'."
  "applicationKey":
    type: string
    required: false
    description: "The application key of the product user groups to search for. Valid values: 'jira-servicedesk', 'jira-software', 'jira-product-discovery', 'jira-core'."
writes: false
expose: false
---
# jira_bulk_get_groups

`GET /rest/api/3/group/bulk` — Bulk get groups

- Request: [[Jira v3 - Bulk get groups]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
