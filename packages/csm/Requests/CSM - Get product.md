---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/product
  - api/operation/get
  - api/effect/read
up: "[[MCP - CSM]]"
app: "CSM"
method: GET
path: "/api/v1/product/{productId}"
category: "Product"
writes_data: false
---
# CSM - Get product

**Get product** — `GET /api/v1/product/{productId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get product"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/product/{{param:productId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `productId` (path, string, required) — Value of productId in the path.

## Original description

**Permissions required:** Jira Service Management agent.
