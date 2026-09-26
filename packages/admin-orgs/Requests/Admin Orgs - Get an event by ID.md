---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/events
  - api/operation/get
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v1/orgs/{orgId}/events/{eventId}"
category: "Events"
writes_data: false
---
# Admin Orgs - Get an event by ID

**Get an event by ID** — `GET /v1/orgs/{orgId}/events/{eventId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get an event by ID"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/events/{{param:eventId}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `eventId` (path, string, required) — ID of the event to return

## Original description

Returns information about a single event by ID.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:events:admin`
