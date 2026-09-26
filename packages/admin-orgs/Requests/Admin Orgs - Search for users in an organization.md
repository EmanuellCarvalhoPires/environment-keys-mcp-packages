---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/users
  - api/operation/search
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: POST
path: "/v2/orgs/{orgId}/directories/{directoryId}/users/search"
category: "Users"
writes_data: false
---
# Admin Orgs - Search for users in an organization

**Search for users in an organization** — `POST /v2/orgs/{orgId}/directories/{directoryId}/users/search`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Search for users in an organization"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
POST https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories/{{param:directoryId}}/users/search
Authorization: {{service.admin_auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `directoryId` (path, string, required) — Unique ID associated with a directory. The - character can be used to increase the operation scope to all directories the requestor has permission to manage.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "searchTerm": "alice",
  "limit": 50
}
```

## Original description

Return a page of users in an organization that match the supplied parameters.

Use `searchTerm` for free-text search across user display names and email addresses. Use `emails` for exact-match filtering by full email addresses. `searchTerm` and `emails` are mutually exclusive. Providing both in the same request returns `400 Bad Request`. Use the `expand` field to include additional fields such as `platformRoles`, `counts.resources`, `productAccess`, and `groups` in the response.
