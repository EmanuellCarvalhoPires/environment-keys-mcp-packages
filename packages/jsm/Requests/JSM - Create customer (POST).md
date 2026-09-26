---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/other-operations
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
app: "JSM"
method: POST
path: "/rest/servicedeskapi/customer/skip-permission-check"
category: "Other operations"
writes_data: true
tool_note: "[[jsm_create_customer_post]]"
---
# JSM - Create customer (POST)

**Create customer** — `POST /rest/servicedeskapi/customer/skip-permission-check`

- Run by the tool [[jsm_create_customer_post]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/customer/skip-permission-check?strictConflictStatusCode={{param:strictConflictStatusCode}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `strictConflictStatusCode` (query, string, optional) — Optional boolean flag; when \{@code true\}, returns 409 Conflict for duplicate email instead of the default 400.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a customer account on behalf of jsd-nutmeg.

This endpoint is restricted to jsd-nutmeg via ASAP authentication. It provides the same capability as the public \{@code POST /servicedeskapi/customer\} endpoint, but does not require a User Context Token (UCT) or Connect app user \\u2014 authorization is enforced entirely via the ASAP token.

No user permission checks are performed; \{@code null\} is passed as the acting user to bypass the permission check in the underlying service.
