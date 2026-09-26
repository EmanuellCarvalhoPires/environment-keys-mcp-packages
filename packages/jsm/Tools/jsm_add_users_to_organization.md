---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_add_users_to_organization
title: "JSM - Add users to organization"
kind: request
request: "[[JSM - Add users to organization]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · POST /rest/servicedeskapi/organization/{organizationId}/user · Add users to organization. This method adds users to an organization. Permissions required: Service desk administrator or agent. Note: Permission to add users to an organization can be switched to users with the Jira administrator permission, using the Organization management feature. Writes data: yes."
params:
  "organizationId":
    type: string
    required: true
    description: "The ID of the organization."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsm_add_users_to_organization

`POST /rest/servicedeskapi/organization/{organizationId}/user` — Add users to organization

- Request: [[JSM - Add users to organization]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
