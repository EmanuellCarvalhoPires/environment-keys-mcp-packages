---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/entitlement
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/status/experimental
up: "[[MCP - CSM]]"
app: "CSM"
method: GET
path: "/api/v1/entitlements"
category: "Entitlement"
writes_data: false
---
# CSM - Get entitlements

**Get entitlements** — `GET /api/v1/entitlements`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get entitlements"`.
- **Experimental:** sends the `X-ExperimentalApi: opt-in` header.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/entitlements?entityType={{param:entityType}}&entityId={{param:entityId}}&start={{param:start}}&limit={{param:limit}}&productId={{param:productId}}
Authorization: {{service.auth_token}}
Accept: application/json
X-ExperimentalApi: opt-in
```

## Parameters

- `entityType` (query, string, required) — The entity type to return entitlements for.
- `entityId` (query, string, required) — The unique identifier for the entity.
- `start` (query, string, optional) — The zero-based index of the first entitlement to return. Defaults to 0 if not specified.
- `limit` (query, string, optional) — The number of entitlements to fetch. Max is 25 and defaults to 25 if not specified.
- `productId` (query, string, optional) — A product ID to optionally filter the entitlements to just entitlements of that product.

## Original description

Returns a paginated list of the customer or organization's entitlements, along with their details. Returns a max of 50 results.
When the entity is a customer, it can be a Customer Account in this site's customer directory or an active Atlassian Account with the CSM customer role that is not a CSM agent or Jira site admin.
To understand which `customerId` values are supported, see [Supported customer IDs](/cloud/customer-service-management/customer-ids).
**Permissions required:** Jira Service Management agent.
