---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer-experience
  - api/operation/list
  - api/effect/read
  - api/status/experimental
up: "[[MCP - CSM]]"
app: "CSM"
method: GET
path: "/api/v1/helpcenter/{helpCenterId}/access/organization"
category: "Customer experience"
writes_data: false
---
# CSM - Get organizations with access to a Customer Experience

**Get organizations with access to a Customer Experience** — `GET /api/v1/helpcenter/{helpCenterId}/access/organization`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get organizations with access to a Customer Experience"`.
- **Experimental:** sends the `X-ExperimentalApi: opt-in` header.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/helpcenter/{{param:helpCenterId}}/access/organization?startAt={{param:startAt}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
X-ExperimentalApi: opt-in
```

## Parameters

- `helpCenterId` (path, string, required) — Value of helpCenterId in the path.
- `startAt` (query, string, optional) — The zero-based index of the first organization to return.
- `limit` (query, string, optional) — The maximum number of organizations to return.

## Original description

Returns the Customer Service Management organizations that have access to a Customer Experience.

The Customer Experience must use organization-restricted access.

**Permissions required:** The caller must be able to administer the Customer Experience.
