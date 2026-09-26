---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_users_in_organization
title: "JSM - Get users in organization"
kind: request
request: "[[JSM - Get users in organization]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/organization/{organizationId}/user · Get users in organization. This method returns all the users associated with an organization. Use this method where you want to provide a list of users for an organization or determine if a user is associated with an organization. Permissions required: Service desk administrator or agent. Writes data: no."
params:
  "organizationId":
    type: string
    required: true
    description: "The ID of the organization."
  "start":
    type: string
    required: false
    description: "The starting index of the returned objects. Base index: 0. See the Pagination section for more details."
  "limit":
    type: string
    required: false
    description: "The maximum number of users to return per page. Default: 50. See the Pagination section for more details."
writes: false
expose: false
---
# jsm_get_users_in_organization

`GET /rest/servicedeskapi/organization/{organizationId}/user` — Get users in organization

- Request: [[JSM - Get users in organization]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
