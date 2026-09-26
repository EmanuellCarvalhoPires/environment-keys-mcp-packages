---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/organization-bulk-operations
  - api/operation/action
  - api/effect/write
up: "[[MCP - CSM]]"
app: "CSM"
method: POST
path: "/api/v1/organization/details/bulk"
category: "Organization bulk operations"
writes_data: true
---
# CSM - Bulk manage organizations' detail field values

**Bulk manage organizations' detail field values** — `POST /api/v1/organization/details/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Bulk manage organizations' detail field values"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/organization/details/bulk
Authorization: {{service.auth_token}}
Accept: application/json
Idempotency-Key: {{param:idempotency_key}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `idempotency_key` (header, string, required) — Value of the `Idempotency-Key` header.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Bulk manage organization detail field values for multiple organizations. Supports UPDATE, PATCH, and DELETE operations across multiple organizations and detail fields. A request can include up to 1000 detail-field operations total, counted across all organizations in the request.
**Permissions required:** Customer Service Management or Jira Service Management user.
