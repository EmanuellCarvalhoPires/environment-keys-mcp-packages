---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/organization
  - api/operation/search
  - api/effect/read
up: "[[MCP - CSM]]"
app: "CSM"
method: POST
path: "/api/v1/organization/fetch"
category: "Organization"
writes_data: false
---
# CSM - Fetch multiple organizations

**Fetch multiple organizations** — `POST /api/v1/organization/fetch`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Fetch multiple organizations"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/organization/fetch
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Returns a maximum of 50 organizations, fetched by organization id or name.
Any organizations that cannot be found will be omitted from the results.
**Permissions required:** Customer Service Management or Jira Service Management user.
