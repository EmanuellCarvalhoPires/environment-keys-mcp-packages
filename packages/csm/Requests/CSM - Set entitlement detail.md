---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/entitlement
  - api/operation/update
  - api/effect/write
up: "[[MCP - CSM]]"
app: "CSM"
method: PUT
path: "/api/v1/entitlement/{entitlementId}/details"
category: "Entitlement"
writes_data: true
---
# CSM - Set entitlement detail

**Set entitlement detail** — `PUT /api/v1/entitlement/{entitlementId}/details`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Set entitlement detail"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
PUT https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/entitlement/{{param:entitlementId}}/details?fieldName={{param:fieldName}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `entitlementId` (path, string, required) — Value of entitlementId in the path.
- `fieldName` (query, string, required) — The name of the entitlement detail field to set the value of.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

**Permissions required:** Jira Service Management agent.
