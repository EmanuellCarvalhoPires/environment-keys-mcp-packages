---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: POST
path: "/api/v1/customer/profile"
category: "Customer"
writes_data: true
---
# CSM - Create customer profile

**Create customer profile** — `POST /api/v1/customer/profile`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Create customer profile"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/profile
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a customer's profile, including their custom details and associating them with the specified organizations and products.
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/), and Customer Service Management or Jira Service Management user.
