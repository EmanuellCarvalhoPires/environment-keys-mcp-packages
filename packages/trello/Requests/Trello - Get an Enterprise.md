---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/enterprises
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/enterprises/{id}"
category: "Enterprises"
writes_data: false
---
# Trello - Get an Enterprise

**Get an Enterprise** — `GET /enterprises/{id}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get an Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/enterprises/{{param:id}}?fields={{param:fields}}&members={{param:members}}&member_fields={{param:member_fields}}&member_filter={{param:member_filter}}&member_sort={{param:member_sort}}&member_sortBy={{param:member_sortBy}}&member_sortOrder={{param:member_sortOrder}}&member_startIndex={{param:member_startIndex}}&member_count={{param:member_count}}&organizations={{param:organizations}}&organization_fields={{param:organization_fields}}&organization_paid_accounts={{param:organization_paid_accounts}}&organization_memberships={{param:organization_memberships}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the enterprise to retrieve.
- `fields` (query, string, optional) — Comma-separated list of: id, name, displayName, prefs, ssoActivationFailed, idAdmins, idMembers (Note that the members array returned will be paginated if members is 'normal' or 'admins'.
- `members` (query, string, optional) — One of: none, normal, admins, owners, all
- `member_fields` (query, string, optional) — One of: avatarHash, fullName, initials, username
- `member_filter` (query, string, optional) — Pass a SCIM-style query to filter members. This takes precedence over the all/normal/admins value of members. If any of the member args are set, the member array will be paginated.
- `member_sort` (query, string, optional) — This parameter expects a SCIM-style sorting value prefixed by a - to sort descending. If no - is prefixed, it will be sorted ascending.
- `member_sortBy` (query, string, optional) — Deprecated: Please use membersort. This parameter expects a SCIM-style sorting value. Note that the members array returned will be paginated if members is normal or admins.
- `member_sortOrder` (query, string, optional) — Deprecated: Please use membersort. One of: ascending, descending, asc, desc
- `member_startIndex` (query, string, optional) — Any integer between 0 and 100.
- `member_count` (query, string, optional) — 0 to 100
- `organizations` (query, string, optional) — One of: none, members, public, all
- `organization_fields` (query, string, optional) — Any valid value that the [nested organization field resource]() accepts.
- `organization_paid_accounts` (query, string, optional) — Whether or not to include paid account information in the returned workspace objects
- `organization_memberships` (query, string, optional) — Comma-seperated list of: me, normal, admin, active, deactivated

## Original description

Get an enterprise by its ID.
