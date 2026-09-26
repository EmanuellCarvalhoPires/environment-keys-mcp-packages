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
path: "/api/v1/organization/{organizationId}"
category: "Organization"
writes_data: false
---
# CSM - Get organization

**Get organization** — `GET /api/v1/organization/{organizationId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get organization"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/organization/{{param:organizationId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `organizationId` (path, string, required) — Value of organizationId in the path.

## Original description

Returns an organization, including its details.
It is recommended to use the [get organization profile API](./#api-api-v1-organization-profile-organizationid-get) which is a simpler response shape to work with and also includes the entitlements for the organization.
**Permissions required:** Jira Service Management agent.
