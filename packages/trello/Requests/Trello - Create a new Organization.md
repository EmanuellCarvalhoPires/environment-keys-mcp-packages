---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/organizations
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/organizations"
category: "Organizations"
writes_data: true
---
# Trello - Create a new Organization

**Create a new Organization** — `POST /organizations`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a new Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/organizations?displayName={{param:displayName}}&desc={{param:desc}}&name={{param:name}}&website={{param:website}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `displayName` (query, string, required) — The name to display for the Organization
- `desc` (query, string, optional) — The description for the organizations
- `name` (query, string, optional) — A string with a length of at least 3. Only lowercase letters, underscores, and numbers are allowed. If the name contains invalid characters, they will be removed.
- `website` (query, string, optional) — A URL starting with http:// or https://

## Original description

Create a new Workspace
