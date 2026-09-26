---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/customer
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - JSM]]"
app: "JSM"
method: PUT
path: "/rest/servicedeskapi/customer/user/{accountId}/revoke-portal-only-access"
category: "Customer"
writes_data: true
tool_note: "[[jsm_revoke_portal_only_access_for_user]]"
---
# JSM - Revoke portal only access for user

**Revoke portal only access for user** — `PUT /rest/servicedeskapi/customer/user/{accountId}/revoke-portal-only-access`

- Run by the tool [[jsm_revoke_portal_only_access_for_user]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
PUT {{service.url}}/rest/servicedeskapi/customer/user/{{param:accountId}}/revoke-portal-only-access
Authorization: {{service.auth_token}}
```

## Parameters

- `accountId` (path, string, required) — The account ID of the user, which uniquely identifies the portal-only account. For example, qm:a713c8ea-1075-4e30-9d96-891a7d181739:5ad6d3581db05e2a66fa80b.

## Original description

This method revokes portal-only access for a particular user, removing their ability to log in to the Jira Service Management customer portal as a portal-only user. After revocation, the user cannot submit or view requests through the portal.

**[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).
