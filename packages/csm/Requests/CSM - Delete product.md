---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/product
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: DELETE
path: "/api/v1/product/{productId}"
category: "Product"
writes_data: true
---
# CSM - Delete product

**Delete product** — `DELETE /api/v1/product/{productId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Delete product"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
DELETE https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/product/{{param:productId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `productId` (path, string, required) — Value of productId in the path.

## Original description

Deletes a product and all entitlements associated with it. You cannot restore a detail field once it has been deleted.
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
