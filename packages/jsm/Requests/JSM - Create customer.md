---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/customer
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
app: "JSM"
method: POST
path: "/rest/servicedeskapi/customer"
category: "Customer"
writes_data: true
tool_note: "[[jsm_create_customer]]"
---
# JSM - Create customer

**Create customer** — `POST /rest/servicedeskapi/customer`

- Run by the tool [[jsm_create_customer]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/customer?strictConflictStatusCode={{param:strictConflictStatusCode}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `strictConflictStatusCode` (query, string, optional) — Optional boolean flag to return 409 Conflict status code for duplicate customer creation request
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "displayName": "Fred F. User",
  "email": "fred@example.com"
}
```

## Original description

This method adds a customer to the Jira Service Management instance by passing a JSON file including an email address and display name. The display name does not need to be unique. The record's identifiers, `name` and `key`, are automatically generated from the request details.

**[Permissions](#permissions) required**: Jira Administrator Global permission
