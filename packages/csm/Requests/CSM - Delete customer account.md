---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: DELETE
path: "/api/v1/customer/account/{customerId}"
category: "Customer"
writes_data: true
---
# CSM - Delete customer account

**Delete customer account** — `DELETE /api/v1/customer/account/{customerId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Delete customer account"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
DELETE https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/account/{{param:customerId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `customerId` (path, string, required) — Value of customerId in the path.

## Original description

Deletes a customer. You cannot restore a customer account once it has been deleted.
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
