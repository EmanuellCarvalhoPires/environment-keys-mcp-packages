---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/groups
  - api/operation/search
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: POST
path: "/v2/orgs/{orgId}/directories/{directoryId}/groups/search"
category: "Groups"
writes_data: false
---
# Admin Orgs - Search for groups in an organization

**Search for groups in an organization** — `POST /v2/orgs/{orgId}/directories/{directoryId}/groups/search`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Search for groups in an organization"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
POST https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/directories/{{param:directoryId}}/groups/search
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
  "searchTerm": "engineering",
  "limit": 20
}
```

## Original description

Return a page of groups in an organization that match the supplied parameters.

Use `searchTerm` for free-text search across group names. Filter by IDs, role assignments, resources, members, or specific group identifiers using the corresponding request fields. Use the `expand` field to include additional fields such as `counts.resources` and `counts.users` in the response.
