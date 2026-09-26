---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/product
  - api/operation/create
  - api/effect/write
up: "[[MCP - CSM]]"
app: "CSM"
method: POST
path: "/api/v1/product"
category: "Product"
writes_data: true
---
# CSM - Create product

**Create product** — `POST /api/v1/product`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Create product"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/product
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

**Permissions required:** Jira Service Management agent.
