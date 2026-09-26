---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/spaces"
category: "Space"
writes_data: true
tool_note: "[[confluence_create_space]]"
---
# Confluence v2 - Create space

**Create space** — `POST /spaces`

- Run by the tool [[confluence_create_space]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/spaces
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a Space as specified in the payload.

Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to create spaces.
