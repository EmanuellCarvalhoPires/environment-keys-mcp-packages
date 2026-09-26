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
path: "/api/{cloudId}/v1/users/contacts/{id}/activate"
category: "Contacts"
writes_data: true
---
# JSM Ops - Activate contact

**Activate contact** — `PATCH /api/{cloudId}/v1/users/contacts/{id}/activate`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Activate contact"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PATCH https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/users/contacts/{{param:id}}/activate
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Activates a contact of a user.
