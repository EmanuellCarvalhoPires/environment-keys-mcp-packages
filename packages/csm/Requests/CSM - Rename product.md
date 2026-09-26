---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/product
  - api/operation/update
  - api/effect/write
up: "[[MCP - CSM]]"
app: "CSM"
method: PUT
path: "/api/v1/product/{productId}"
category: "Product"
writes_data: true
---
# CSM - Rename product

**Rename product** — `PUT /api/v1/product/{productId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Rename product"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
PUT https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/product/{{param:productId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `productId` (path, string, required) — Value of productId in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

**Permissions required:** Jira Service Management agent.
