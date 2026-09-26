---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/organization
  - api/operation/get
  - api/effect/read
up: "[[MCP - CSM]]"
app: "CSM"
method: GET
path: "/api/v1/organization/profile/{organizationId}"
category: "Organization"
writes_data: false
---
# CSM - Get organization profile

**Get organization profile** — `GET /api/v1/organization/profile/{organizationId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get organization profile"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/organization/profile/{{param:organizationId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `organizationId` (path, string, required) — Value of organizationId in the path.

## Original description

Returns a organization's profile, including its custom details and any product entitlements.
**Permissions required:** Customer Service Management or Jira Service Management user.
