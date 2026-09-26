---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM]]"
tool: jsm_remove_users_from_organization
title: "JSM - Remove users from organization"
kind: request
request: "[[JSM - Remove users from organization]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · DELETE /rest/servicedeskapi/organization/{organizationId}/user · Remove users from organization. This method removes users from an organization. Permissions required: Service desk administrator or agent. Note: Permission to delete users from an organization can be switched to users with the Jira administrator permission, using the Organization management feature. Writes data: yes."
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
# jsm_remove_users_from_organization

`DELETE /rest/servicedeskapi/organization/{organizationId}/user` — Remove users from organization

- Request: [[JSM - Remove users from organization]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
