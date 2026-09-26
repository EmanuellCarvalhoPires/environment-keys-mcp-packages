---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer-bulk-operations
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: POST
path: "/api/v1/customer/details/bulk"
category: "Customer bulk operations"
writes_data: true
---
# CSM - Bulk manage customers' detail field values

**Bulk manage customers' detail field values** — `POST /api/v1/customer/details/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Bulk manage customers' detail field values"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/details/bulk
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

Bulk manage customer detail field values for multiple customers. Supports UPDATE, PATCH, and DELETE operations across multiple customers and detail fields. A customer can be a Customer Account in this site's customer directory or an active Atlassian Account with the CSM customer role that is not a CSM agent or Jira site admin. A request can include up to 1000 detail-field operations total, counted across all customers in the request.
To understand which `customerId` values are supported, see [Supported customer IDs](/cloud/customer-service-management/customer-ids).
**Permissions required:** Customer Service Management or Jira Service Management user.
