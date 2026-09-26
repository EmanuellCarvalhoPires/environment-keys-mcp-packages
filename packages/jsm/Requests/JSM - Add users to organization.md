---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/organization
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
app: "JSM"
method: POST
path: "/rest/servicedeskapi/organization/{organizationId}/user"
category: "Organization"
writes_data: true
tool_note: "[[jsm_add_users_to_organization]]"
---
# JSM - Add users to organization

**Add users to organization** — `POST /rest/servicedeskapi/organization/{organizationId}/user`

- Run by the tool [[jsm_add_users_to_organization]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/organization/{{param:organizationId}}/user
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `organizationId` (path, string, required) — The ID of the organization.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "accountIds": [
    "qm:a713c8ea-1075-4e30-9d96-891a7d181739:5ad6d3581db05e2a66fa80b",
    "qm:a713c8ea-1075-4e30-9d96-891a7d181739:5ad6d3a01db05e2a66fa80bd"
  ],
  "usernames": []
}
```

## Original description

This method adds users to an organization.

**[Permissions](#permissions) required**: Service desk administrator or agent. Note: Permission to add users to an organization can be switched to users with the Jira administrator permission, using the **[Organization management](https://confluence.atlassian.com/servicedeskcloud/setting-up-service-desk-users-732528877.html#Settingupservicedeskusers-manageorgsManageorganizations)** feature.
