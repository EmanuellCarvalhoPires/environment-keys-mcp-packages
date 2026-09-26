---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer-experience
  - api/operation/action
  - api/effect/write
  - api/status/experimental
up: "[[MCP - CSM]]"
app: "CSM"
method: POST
path: "/api/v1/helpcenter/{helpCenterId}/access/organization"
category: "Customer experience"
writes_data: true
---
# CSM - Grant organizations access to a Customer Experience

**Grant organizations access to a Customer Experience** — `POST /api/v1/helpcenter/{helpCenterId}/access/organization`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Grant organizations access to a Customer Experience"`.
- **Experimental:** sends the `X-ExperimentalApi: opt-in` header.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/helpcenter/{{param:helpCenterId}}/access/organization
Authorization: {{service.auth_token}}
X-ExperimentalApi: opt-in
Content-Type: application/json

{{param:body}}
```

## Parameters

- `helpCenterId` (path, string, required) — Value of helpCenterId in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Grants up to 5 existing Customer Service Management organizations access to a Customer Experience.

The Customer Experience must already use organization-restricted access. This operation does not change a public Customer Experience to restricted access.

**Permissions required:** The caller must be able to view the organization and administer the Customer Experience.
