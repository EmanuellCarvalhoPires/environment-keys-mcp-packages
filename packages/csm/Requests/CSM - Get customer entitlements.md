---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer
  - api/operation/list
  - api/effect/read
up: "[[MCP - CSM]]"
app: "CSM"
method: GET
path: "/api/v1/customer/{customerId}/entitlement"
category: "Customer"
writes_data: false
---
# CSM - Get customer entitlements

**Get customer entitlements** — `GET /api/v1/customer/{customerId}/entitlement`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get customer entitlements"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/{{param:customerId}}/entitlement?product={{param:product}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `customerId` (path, string, required) — Value of customerId in the path.
- `product` (query, string, optional) — A product ID to optionally filter the entitlements to just entitlements of that product.

## Original description

Returns a list of the customer's entitlements, including entitlements inherited by any organizations the customer is in, along with their details.
To understand which `customerId` values are supported, see [Supported customer IDs](/cloud/customer-service-management/customer-ids).
**Permissions required:** Jira Service Management agent.
