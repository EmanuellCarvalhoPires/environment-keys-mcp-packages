---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/organization
  - api/operation/update
  - api/effect/write
up: "[[MCP - CSM]]"
app: "CSM"
method: PUT
path: "/api/v1/organization/{organizationId}/details"
category: "Organization"
writes_data: true
---
# CSM - Set organization detail

**Set organization detail** — `PUT /api/v1/organization/{organizationId}/details`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Set organization detail"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
PUT https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/organization/{{param:organizationId}}/details?fieldName={{param:fieldName}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `organizationId` (path, string, required) — Value of organizationId in the path.
- `fieldName` (query, string, required) — The name of the organization detail field to set the value of.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

**Permissions required:** Jira Service Management agent.
