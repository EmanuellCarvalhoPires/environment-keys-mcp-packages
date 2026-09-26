---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/contacts
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/users/contacts/{id}"
category: "Contacts"
writes_data: false
---
# JSM Ops - Get contact

**Get contact** — `GET /api/{cloudId}/v1/users/contacts/{id}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get contact"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/users/contacts/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Returns the details of a contact.
