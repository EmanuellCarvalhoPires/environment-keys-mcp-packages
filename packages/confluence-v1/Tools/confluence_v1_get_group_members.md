---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/group
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_get_group_members
title: "Confluence v1 - Get group members"
kind: request
request: "[[Confluence v1 - Get group members]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/group/{groupId}/membersByGroupId · Get group members. Returns the users that are members of a group. Use updated Get group API Permissions required: Permission to access the Confluence site ('Can use' global permission). Writes data: no."
params:
  "groupId":
    type: string
    required: true
    description: "The id of the group to be queried for its members."
  "start":
    type: string
    required: false
    description: "The starting index of the returned users."
  "limit":
    type: string
    required: false
    description: "The maximum number of users to return per page. Note, this may be restricted by fixed system limits."
  "shouldReturnTotalSize":
    type: string
    required: false
    description: "Whether to include total size parameter in the results. Note, fetching total size property is an expensive operation; use it if your use case needs this value."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the user to expand. - operations returns the operations that the user is allowed to do."
writes: false
expose: false
---
# confluence_v1_get_group_members

`GET /wiki/rest/api/group/{groupId}/membersByGroupId` — Get group members

- Request: [[Confluence v1 - Get group members]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
