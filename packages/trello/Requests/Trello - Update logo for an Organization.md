---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/organizations
  - api/operation/action
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/organizations/{id}/logo"
category: "Organizations"
writes_data: true
---
# Trello - Update logo for an Organization

**Update logo for an Organization** — `POST /organizations/{id}/logo`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update logo for an Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/organizations/{{param:id}}/logo?file={{param:file}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or name of the Workspace
- `file` (query, string, optional) — Image file for the logo

## Original description

Set the logo image for a Workspace
