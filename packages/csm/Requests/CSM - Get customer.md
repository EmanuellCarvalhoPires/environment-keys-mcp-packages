---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer
  - api/operation/get
  - api/effect/read
up: "[[MCP - CSM]]"
app: "CSM"
method: GET
path: "/api/v1/customer/{customerId}"
category: "Customer"
writes_data: false
---
# CSM - Get customer

**Get customer** — `GET /api/v1/customer/{customerId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get customer"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/{{param:customerId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `customerId` (path, string, required) — Value of customerId in the path.

## Original description

Returns a customer, including their details.
It is recommended to use the [get customer profile API](./#api-api-v1-customer-profile-customerid-get) which is a simpler response shape to work with and also includes the entitlements for the customer.
To understand which `customerId` values are supported, see [Supported customer IDs](/cloud/customer-service-management/customer-ids).
**Permissions required:** Jira Service Management agent.
