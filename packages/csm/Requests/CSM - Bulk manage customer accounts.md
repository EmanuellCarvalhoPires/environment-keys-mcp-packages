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
path: "/api/v1/customer/bulk"
category: "Customer bulk operations"
writes_data: true
---
# CSM - Bulk manage customer accounts

**Bulk manage customer accounts** — `POST /api/v1/customer/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Bulk manage customer accounts"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/bulk
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

Bulk manage multiple customer accounts. This allows up to 50 customer accounts in a single request.
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
