---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer
  - api/operation/list
  - api/effect/read
  - api/status/experimental
up: "[[MCP - CSM]]"
app: "CSM"
method: GET
path: "/api/v1/customer/{customerId}/customer-experiences"
category: "Customer"
writes_data: false
---
# CSM - Get customer accessible customer experiences

**Get customer accessible customer experiences** — `GET /api/v1/customer/{customerId}/customer-experiences`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get customer accessible customer experiences"`.
- **Experimental:** sends the `X-ExperimentalApi: opt-in` header.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/{{param:customerId}}/customer-experiences
Authorization: {{service.auth_token}}
Accept: application/json
X-ExperimentalApi: opt-in
```

## Parameters

- `customerId` (path, string, required) — Value of customerId in the path.

## Original description

Returns the Customer Experiences that the given customer can access.

**Permissions required:** Customer Service Management agent.
