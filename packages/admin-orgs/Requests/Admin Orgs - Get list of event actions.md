---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/events
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v1/orgs/{orgId}/event-actions"
category: "Events"
writes_data: false
---
# Admin Orgs - Get list of event actions

**Get list of event actions** — `GET /v1/orgs/{orgId}/event-actions`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get list of event actions"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/event-actions
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Original description

Returns information localized event actions

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:events:admin`
