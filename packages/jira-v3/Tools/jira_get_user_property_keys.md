---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-properties
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_user_property_keys
title: "Jira v3 - Get user property keys"
kind: request
request: "[[Jira v3 - Get user property keys]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/user/properties · Get user property keys. Returns the keys of all properties for a user. Note: This operation does not access the user properties created and maintained in Jira. Permissions required: Administer Jira global permission, to access the property keys on any user. Writes data: no."
params:
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
# jira_get_user_property_keys

`GET /rest/api/3/user/properties` — Get user property keys

- Request: [[Jira v3 - Get user property keys]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
