---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/customer
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - JSM]]"
tool: jsm_revoke_portal_only_access_for_user
title: "JSM - Revoke portal only access for user"
kind: request
request: "[[JSM - Revoke portal only access for user]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · PUT /rest/servicedeskapi/customer/user/{accountId}/revoke-portal-only-access · Revoke portal only access for user. This method revokes portal-only access for a particular user, removing their ability to log in to the Jira Service Management customer portal as a portal-only user. After revocation, the user cannot submit or view requests through the portal. Writes data: yes."
params:
  "accountId":
    type: string
    required: true
    description: "The account ID of the user, which uniquely identifies the portal-only account. For example, qm:a713c8ea-1075-4e30-9d96-891a7d181739:5ad6d3581db05e2a66fa80b."
writes: true
expose: false
---
# jsm_revoke_portal_only_access_for_user

`PUT /rest/servicedeskapi/customer/user/{accountId}/revoke-portal-only-access` — Revoke portal only access for user

- Request: [[JSM - Revoke portal only access for user]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
