---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-properties
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_user_property
title: "Jira v3 - Delete user property"
kind: request
request: "[[Jira v3 - Delete user property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/user/properties/{propertyKey} · Delete user property. Deletes a property from a user. Note: This operation does not access the user properties created and maintained in Jira. Permissions required: Administer Jira global permission, to delete a property from any user. Writes data: yes."
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
writes: true
expose: false
---
# jira_delete_user_property

`DELETE /rest/api/3/user/properties/{propertyKey}` — Delete user property

- Request: [[Jira v3 - Delete user property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
