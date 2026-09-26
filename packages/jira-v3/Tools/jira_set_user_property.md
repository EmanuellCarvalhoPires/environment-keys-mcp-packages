---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-properties
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_set_user_property
title: "Jira v3 - Set user property"
kind: request
request: "[[Jira v3 - Set user property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/user/properties/{propertyKey} · Set user property. Sets the value of a user's property. Use this resource to store custom data against a user. Note: This operation does not access the user properties created and maintained in Jira. Permissions required: Administer Jira global permission, to set a property on any user. Writes data: yes."
params:
  "propertyKey":
    type: string
    required: true
    description: "The key of the user's property. The maximum length is 255 characters."
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
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_user_property

`PUT /rest/api/3/user/properties/{propertyKey}` — Set user property

- Request: [[Jira v3 - Set user property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
