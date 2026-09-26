---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer-experience
  - api/operation/delete
  - api/effect/write
  - api/status/experimental
up: "[[MCP - CSM]]"
app: "CSM"
method: DELETE
path: "/api/v1/helpcenter/{helpCenterId}/access/organization/{organizationId}"
category: "Customer experience"
writes_data: true
---
# CSM - Remove an organization from a Customer Experience

**Remove an organization from a Customer Experience** — `DELETE /api/v1/helpcenter/{helpCenterId}/access/organization/{organizationId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Remove an organization from a Customer Experience"`.
- **Experimental:** sends the `X-ExperimentalApi: opt-in` header.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
DELETE https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/helpcenter/{{param:helpCenterId}}/access/organization/{{param:organizationId}}
Authorization: {{service.auth_token}}
X-ExperimentalApi: opt-in
```

## Parameters

- `helpCenterId` (path, string, required) — Value of helpCenterId in the path.
- `organizationId` (path, string, required) — Value of organizationId in the path.

## Original description

Removes an existing Customer Service Management organization's access to a Customer Experience.

The Customer Experience must use organization-restricted access. If the organization does not currently have access, no change is made.

**Permissions required:** The caller must be able to view the organization and administer the Customer Experience.
