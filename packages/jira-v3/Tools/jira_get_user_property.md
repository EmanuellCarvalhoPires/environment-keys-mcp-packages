---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-properties
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_user_property
title: "Jira v3 - Get user property"
kind: request
request: "[[Jira v3 - Get user property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/user/properties/{propertyKey} · Get user property. Returns the value of a user's property. If no property key is provided Get user property keys is called. Note: This operation does not access the user properties created and maintained in Jira. Writes data: no."
params:
  "propertyKey":
    type: string
    required: true
    description: "The key of the user's property."
  "accountId":
    type: string
    required: false
    description: "The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5."
  "userKey":
    type: string
    required: false
    description: "This parameter is no longer available and will be removed from the documentation soon. See the deprecation notice for details."
  "username":
    type: string
    required: false
    description: "This parameter is no longer available and will be removed from the documentation soon. See the deprecation notice for details."
writes: false
expose: false
---
# jira_get_user_property

`GET /rest/api/3/user/properties/{propertyKey}` — Get user property

- Request: [[Jira v3 - Get user property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
