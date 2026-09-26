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
path: "/api/v1/entitlement/{entitlementId}"
category: "Entitlement"
writes_data: true
---
# CSM - Delete entitlement

**Delete entitlement** — `DELETE /api/v1/entitlement/{entitlementId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Delete entitlement"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
DELETE https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/entitlement/{{param:entitlementId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `entitlementId` (path, string, required) — Value of entitlementId in the path.

## Original description

Deletes the specified entitlement along with its detail fields. You cannot restore an entitlement once it has been deleted.
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
