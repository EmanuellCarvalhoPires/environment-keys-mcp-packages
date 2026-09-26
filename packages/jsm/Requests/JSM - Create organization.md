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
path: "/rest/servicedeskapi/organization"
category: "Organization"
writes_data: true
tool_note: "[[jsm_create_organization]]"
---
# JSM - Create organization

**Create organization** — `POST /rest/servicedeskapi/organization`

- Run by the tool [[jsm_create_organization]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/organization
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "name": "Charlie Cakes Franchises"
}
```

## Original description

This method creates an organization by passing the name of the organization.

**[Permissions](#permissions) required**: Service desk administrator or agent. Note: Permission to create organizations can be switched to users with the Jira administrator permission, using the **[Organization management](https://confluence.atlassian.com/servicedeskcloud/setting-up-service-desk-users-732528877.html#Settingupservicedeskusers-manageorgsManageorganizations)** feature.
