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
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/customer/skip-permission-check"
category: "Other operations"
writes_data: true
tool_note: "[[jsm_add_customers_post]]"
---
# JSM - Add customers (POST)

**Add customers** — `POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer/skip-permission-check`

- Run by the tool [[jsm_add_customers_post]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/customer/skip-permission-check
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk to add customers to. This can alternatively be a project identifier.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Adds one or more customers to a service desk on behalf of jsd-nutmeg.

This endpoint is restricted to jsd-nutmeg via ASAP authentication. It provides the same capability as the public \{@code POST /servicedeskapi/servicedesk/\{serviceDeskId\}/customer\} endpoint, but does not require a User Context Token (UCT) or Connect app user \\u2014 authorization is enforced entirely via the ASAP token.

No user permission checks are performed; \{@code null\} is passed as the acting user to bypass the permission check in the underlying service.

If any of the passed customers are already associated with the service desk, no changes will be made for those customers and the resource returns a 204 success code.
