---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/product
  - api/operation/list
  - api/effect/read
up: "[[MCP - CSM]]"
app: "CSM"
method: GET
path: "/api/v1/product"
category: "Product"
writes_data: false
---
# CSM - Get products

**Get products** — `GET /api/v1/product`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get products"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/product?limit={{param:limit}}&cursor={{param:cursor}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `limit` (query, string, optional) — The number of products to fetch. Defaults to 100 if not specified or value given is less than 1 or greater than 100.
- `cursor` (query, string, optional) — The starting point for the page of results to return. Use the value of nextPageCursor in one request to get the next page.

## Original description

**Permissions required:** Jira Service Management agent.
