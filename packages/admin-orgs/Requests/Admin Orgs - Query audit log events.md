---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/events
  - api/operation/search
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v1/orgs/{orgId}/events"
category: "Events"
writes_data: false
---
# Admin Orgs - Query audit log events

**Query audit log events** — `GET /v1/orgs/{orgId}/events`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Query audit log events"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/events?cursor={{param:cursor}}&q={{param:q}}&from={{param:from}}&to={{param:to}}&action={{param:action}}&actor={{param:actor}}&ip={{param:ip}}&product={{param:product}}&location={{param:location}}&limit={{param:limit}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `cursor` (query, string, optional) — Sets the starting point for the page of results to return
- `q` (query, string, optional) — Single query term for searching events.
- `from` (query, string, optional) — The earliest date and time of the event represented as a UNIX epoch time in milliseconds.
- `to` (query, string, optional) — The latest date and time of the event represented as a UNIX epoch time in milliseconds.
- `action` (query, string, optional) — A query filter that returns events of a specific action type.
- `actor` (query, string, optional) — A query filter that returns events by one or more specific actors.
- `ip` (query, string, optional) — A query filter that returns events by one or more specific ip addresses.
- `product` (query, string, optional) — A query filter that returns events by one or more specific products.
- `location` (query, string, optional) — A query filter that returns events by one or more specific locations. Of format: [ { "city": "", "countryName": "" }, ... ]
- `limit` (query, string, optional) — The maximum number of events to return per page.

## Original description

Returns a filtered list of audit log events for an organization.
Use this endpoint for more granular and detailed querying. 

If you simply need to paginate through all events, consider using the [/events-stream](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-events/#api-v1-orgs-orgid-events-stream-get) endpoint.  

These rate limits for this endpoint be lowered effective end of May 2025 as follows:
 - *Rate limit per user*: *10* requests per minute
 - *Rate limit per API path*: *10* requests per minute

 Please migrate to the polling API to guarantee uninterrupted service for use cases involving a high request rate.

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:events:admin`
