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
path: "/api/v1/customer/details/{fieldName}"
category: "Customer"
writes_data: true
---
# CSM - Delete customer detail field

**Delete customer detail field** — `DELETE /api/v1/customer/details/{fieldName}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Delete customer detail field"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
DELETE https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/details/{{param:fieldName}}
Authorization: {{service.auth_token}}
```

## Parameters

- `fieldName` (path, string, required) — Value of fieldName in the path.

## Original description

Deletes a customer detail field and all values stored for it for all customers. You cannot restore a detail field once it has been deleted.
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
