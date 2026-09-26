---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/entitlement
  - api/operation/get
  - api/effect/read
up: "[[MCP - CSM]]"
app: "CSM"
method: GET
path: "/api/v1/entitlement/{entitlementId}"
category: "Entitlement"
writes_data: false
---
# CSM - Get entitlement

**Get entitlement** — `GET /api/v1/entitlement/{entitlementId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get entitlement"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/entitlement/{{param:entitlementId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `entitlementId` (path, string, required) — Value of entitlementId in the path.

## Original description

Returns an entitlement, including its details. You can get entitlements for a customer using the [get customer entitlements](../api-group-customer/#api-api-v1-customer-customerid-get) API,
and get entitlements for an organization using the [get organization entitlements](../api-group-organization/#api-api-v1-organization-organizationid-get) API.
**Permissions required:** Jira Service Management agent.
