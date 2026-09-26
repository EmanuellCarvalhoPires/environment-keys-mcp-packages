---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/entitlement
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: DELETE
path: "/api/v1/entitlement/details/{fieldName}"
category: "Entitlement"
writes_data: true
---
# CSM - Delete entitlement detail field

**Delete entitlement detail field** — `DELETE /api/v1/entitlement/details/{fieldName}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Delete entitlement detail field"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
DELETE https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/entitlement/details/{{param:fieldName}}
Authorization: {{service.auth_token}}
```

## Parameters

- `fieldName` (path, string, required) — Value of fieldName in the path.

## Original description

Deletes an entitlement detail field and all values stored for it for all entitlements. You cannot restore a detail field once it has been deleted.
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
