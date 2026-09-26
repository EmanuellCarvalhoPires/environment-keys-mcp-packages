---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/organization
  - api/operation/list
  - api/effect/read
up: "[[MCP - CSM]]"
app: "CSM"
method: GET
path: "/api/v1/organization/{organizationId}/entitlement"
category: "Organization"
writes_data: false
---
# CSM - Get organization entitlements

**Get organization entitlements** — `GET /api/v1/organization/{organizationId}/entitlement`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get organization entitlements"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/organization/{{param:organizationId}}/entitlement?product={{param:product}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `organizationId` (path, string, required) — Value of organizationId in the path.
- `product` (query, string, optional) — A product ID to optionally filter the entitlements to just entitlements of that product.

## Original description

Returns a list of the organization's entitlements, along with their details.
**Permissions required:** Jira Service Management agent.
