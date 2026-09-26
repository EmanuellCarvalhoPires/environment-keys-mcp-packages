---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/contacts
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PATCH
path: "/api/{cloudId}/v1/users/contacts/{id}"
category: "Contacts"
writes_data: true
---
# JSM Ops - Update contact

**Update contact** — `PATCH /api/{cloudId}/v1/users/contacts/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update contact"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PATCH https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/users/contacts/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update the details of a contact of a user. This method can be applied only to email contacts.
