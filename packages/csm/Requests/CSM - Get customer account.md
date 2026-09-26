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
path: "/api/v1/customer/account/{customerId}"
category: "Customer"
writes_data: false
---
# CSM - Get customer account

**Get customer account** — `GET /api/v1/customer/account/{customerId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get customer account"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/account/{{param:customerId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `customerId` (path, string, required) — Value of customerId in the path.

## Original description

Returns a Customer Account's account information.
This endpoint supports only Customer Accounts in this site's customer directory. Atlassian Accounts are not supported because this resource is part of the Customer Account lifecycle API. Use the customer or customer profile APIs to retrieve the customer context for an eligible Atlassian Account.
**Permissions required:** Customer Service Management or Jira Service Management user.
