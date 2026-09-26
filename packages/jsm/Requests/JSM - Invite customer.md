---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
app: "JSM"
method: POST
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/customer/invite"
category: "Servicedesk"
writes_data: true
tool_note: "[[jsm_invite_customer]]"
---
# JSM - Invite customer

**Invite customer** — `POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer/invite`

- Run by the tool [[jsm_invite_customer]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/customer/invite?strictConflictStatusCode={{param:strictConflictStatusCode}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk to which the newly created customer should be added.
- `strictConflictStatusCode` (query, string, optional) — Optional boolean flag to return 409 Conflict status code when a customer with the same email already exists.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "displayName": "Fred F. User",
  "email": "fred@example.com"
}
```

## Original description

This method invites a customer to a specified service desk by sending them an email invitation, creating a new customer account if one does not already exist. The display name does not need to be unique. The record's identifiers, `name` and `key`, are automatically generated from the request details.

**[Permissions](#permissions) required**: Jira Administrator Global permission & Service desk administrator
