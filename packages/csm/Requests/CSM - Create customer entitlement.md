---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer
  - api/operation/create
  - api/effect/write
up: "[[MCP - CSM]]"
app: "CSM"
method: POST
path: "/api/v1/customer/{customerId}/entitlement"
category: "Customer"
writes_data: true
---
# CSM - Create customer entitlement

**Create customer entitlement** — `POST /api/v1/customer/{customerId}/entitlement`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Create customer entitlement"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/{{param:customerId}}/entitlement
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `customerId` (path, string, required) — Value of customerId in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

To understand which `customerId` values are supported, see [Supported customer IDs](/cloud/customer-service-management/customer-ids).
**Permissions required:** Jira Service Management agent.
