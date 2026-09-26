---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: POST
path: "/api/v1/customer/profile/fetch"
category: "Customer"
writes_data: false
---
# CSM - Fetch multiple customer profiles

**Fetch multiple customer profiles** — `POST /api/v1/customer/profile/fetch`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Fetch multiple customer profiles"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/profile/fetch
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Returns a maximum of 25 customer profiles. This includes detail fields and any organizations the customer is in.
A customer can be a Customer Account in this site's customer directory or an active Atlassian Account with the CSM customer role that is not a CSM agent or Jira site admin.
Any requested account that cannot be found or is not an eligible customer will be omitted from the results.
To understand which `customerId` values are supported, see [Supported customer IDs](/cloud/customer-service-management/customer-ids).
**Permissions required:** Customer Service Management or Jira Service Management user.
