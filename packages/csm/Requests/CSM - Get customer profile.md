---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: GET
path: "/api/v1/customer/profile/{customerId}"
category: "Customer"
writes_data: false
---
# CSM - Get customer profile

**Get customer profile** — `GET /api/v1/customer/profile/{customerId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get customer profile"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/profile/{{param:customerId}}?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `customerId` (path, string, required) — Value of customerId in the path.
- `expand` (query, string, optional) — Use accessibleCustomerExperiences to include the Customer Experiences accessible to the customer. This expansion requires a Customer Service Management user.

## Original description

Returns a customer's profile, including their custom details, any organizations the customer is in, and any customer entitlements.
The customer can be a Customer Account in this site's customer directory or an active Atlassian Account with the CSM customer role that is not a CSM agent or Jira site admin.
To understand which `customerId` values are supported, see [Supported customer IDs](/cloud/customer-service-management/customer-ids).
**Permissions required:** Customer Service Management or Jira Service Management user. The `accessibleCustomerExperiences` expansion additionally requires Customer Service Management user.
