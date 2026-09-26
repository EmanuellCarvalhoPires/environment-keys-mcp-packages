---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: PUT
path: "/api/v1/customer/account/{customerId}"
category: "Customer"
writes_data: true
---
# CSM - Update customer account

**Update customer account** — `PUT /api/v1/customer/account/{customerId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Update customer account"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
PUT https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/account/{{param:customerId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `customerId` (path, string, required) — Value of customerId in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates a customer account's display name.
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
