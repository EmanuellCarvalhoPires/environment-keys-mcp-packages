---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/organization
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: DELETE
path: "/api/v1/organization/{organizationId}"
category: "Organization"
writes_data: true
---
# CSM - Delete organization

**Delete organization** — `DELETE /api/v1/organization/{organizationId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Delete organization"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
DELETE https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/organization/{{param:organizationId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `organizationId` (path, string, required) — Value of organizationId in the path.

## Original description

Deletes an organization. You cannot restore an organization once it has been deleted.
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
