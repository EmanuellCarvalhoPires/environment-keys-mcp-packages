---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/admin-key
  - api/operation/action
  - api/effect/write
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/admin-key"
category: "Admin Key"
writes_data: true
tool_note: "[[confluence_enable_admin_key]]"
---
# Confluence v2 - Enable Admin Key

**Enable Admin Key** — `POST /admin-key`

- Run by the tool [[confluence_enable_admin_key]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/admin-key
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Enables admin key access for the calling user within the site. If an admin key already exists for the user, a new one will be issued with an updated expiration time.

**Note:** The `durationInMinutes` field within the request body is optional. If the request body is empty or if the `durationInMinutes` is set to 0 minutes, a new admin key will be issued to the calling user with a default duration of 10 minutes.

**[Permissions](https://support.atlassian.com/user-management/docs/give-users-admin-permissions/#Centralized-user-management-content) required**:
User must be an organization or site admin.
