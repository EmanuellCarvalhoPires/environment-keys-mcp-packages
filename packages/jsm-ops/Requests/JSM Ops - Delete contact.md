---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/contacts
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/users/contacts/{id}"
category: "Contacts"
writes_data: true
---
# JSM Ops - Delete contact

**Delete contact** — `DELETE /api/{cloudId}/v1/users/contacts/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete contact"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/users/contacts/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Delete a contact of a user.
