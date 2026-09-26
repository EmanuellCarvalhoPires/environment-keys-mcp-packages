---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/workspaces
  - api/operation/search
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: POST
path: "/v2/orgs/{orgId}/workspaces"
category: "Workspaces"
writes_data: false
---
# Admin Orgs - Get list of workspaces

**Get list of workspaces** — `POST /v2/orgs/{orgId}/workspaces`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - Get list of workspaces"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
POST https://api.atlassian.com/admin/v2/orgs/{{service.org_id}}/workspaces
Authorization: {{service.admin_auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "cursor": "c29tZS1iYXNlLTY0LWVuY29kZWQtY3Vyc29y"
}
```

## Original description

A workspace refers to a specific instance of an Atlassian product that is accessed through a unique URL. Whenever a user initiates or adds a new product instance, it results in the creation of a distinct workspace.

This API will:
- Return a paginated list of workspaces in a given org
- Return more details about an organization's products (including product URL).

#### Scopes
**[Authorization scopes](/cloud/admin/scopes/) required:** `read:workspaces:admin`
