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
path: "/api/v1/customer/profile/bulk"
category: "Customer bulk operations"
writes_data: true
---
# CSM - Bulk manage multiple customer profiles

**Bulk manage multiple customer profiles** — `POST /api/v1/customer/profile/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Bulk manage multiple customer profiles"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/profile/bulk
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

Bulk manage multiple customer profiles with detail fields and organization associations.
Allows creating, updating or upserting up to 100 customer profiles in a single request.
**Eligible customers:** Updates can target a Customer Account in this site's customer directory or an active Atlassian Account with the CSM customer role that is not a CSM agent or Jira site admin.
**Customer identification:** To identify Customer Accounts, provide either `email` or `customerId`. Eligible Atlassian Accounts must be identified by `customerId`. When using UPSERT, providing only `customerId` will not create a customer if it doesn't exist. The `email` field must be provided to create a new Customer Account.
**Customer Account lifecycle:** CREATE operations and UPSERT operations that create an account create Customer Accounts only. Atlassian Account display names cannot be updated through this API; eligible Atlassian Accounts can have details, organization associations, and product associations updated.
To understand which `customerId` values are supported, see [Supported customer IDs](/cloud/customer-service-management/customer-ids).
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/), and Customer Service Management or Jira Service Management user.
