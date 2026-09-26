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
path: "/v1/orgs/{orgId}/events-stream"
category: "Events"
writes_data: false
---
# Admin Orgs - Poll audit log events

**Poll audit log events** — `GET /v1/orgs/{orgId}/events-stream`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Poll audit log events"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/events-stream?cursor={{param:cursor}}&from={{param:from}}&to={{param:to}}&limit={{param:limit}}&sortOrder={{param:sortOrder}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `cursor` (query, string, optional) — Sets the starting point for the page of results to return. Can be used when last page is reached to poll for new events. The sort order is maintained in the cursor across requests.
- `from` (query, string, optional) — The earliest date and time of the event represented as a UNIX epoch time in milliseconds.
- `to` (query, string, optional) — The latest date and time of the event represented as a UNIX epoch time in milliseconds.
- `limit` (query, string, optional) — The maximum number of events to return per page.
- `sortOrder` (query, string, optional) — The order used to sort events by processing time. Defaults to ascending.

## Original description

Returns a paginated list of audit logs events for an organization. Use this endpoint if you want to retrieve events in a simple, paginated manner with time-based filtering.

If you need more advanced filtering, refer to the [/events](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-events/#api-v1-orgs-orgid-events-get) endpoint.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:events:admin`
