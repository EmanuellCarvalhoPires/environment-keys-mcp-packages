---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer
  - api/operation/update
  - api/effect/write
up: "[[MCP - CSM]]"
app: "CSM"
method: PUT
path: "/api/v1/customer/{customerId}/details"
category: "Customer"
writes_data: true
---
# CSM - Set customer detail

**Set customer detail** — `PUT /api/v1/customer/{customerId}/details`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Set customer detail"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
PUT https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/{{param:customerId}}/details?fieldName={{param:fieldName}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `customerId` (path, string, required) — Value of customerId in the path.
- `fieldName` (query, string, required) — The name of the customer detail field to set the value of.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

To understand which `customerId` values are supported, see [Supported customer IDs](/cloud/customer-service-management/customer-ids).
**Permissions required:** Jira Service Management agent.
