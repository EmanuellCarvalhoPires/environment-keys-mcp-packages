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
path: "/api/v1/customer/details/definitions/bulk"
category: "Customer bulk operations"
writes_data: true
---
# CSM - Bulk create customer detail field definitions

**Bulk create customer detail field definitions** — `POST /api/v1/customer/details/definitions/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Bulk create customer detail field definitions"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/details/definitions/bulk
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

Create up to 50 customer detail-field definitions in a single async task. You can create up to 50 detail fields. Each detail field name in the request must be unique &mdash; both within the request itself (case-insensitive, trimmed) and against the names of detail fields that already exist on the customer entity. If any name is already in use, the entire request is rejected with `400 Bad Request` and no fields are created. This API does not modify or replace existing definitions.
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
