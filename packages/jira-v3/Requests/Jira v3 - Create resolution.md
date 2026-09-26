---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-resolutions
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/resolution"
category: "Issue resolutions"
writes_data: true
tool_note: "[[jira_create_resolution]]"
---
# Jira v3 - Create resolution

**Create resolution** — `POST /rest/api/3/resolution`

- Run by the tool [[jira_create_resolution]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/resolution
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "My resolution description",
  "name": "My new resolution"
}
```

## Original description

Creates an issue resolution.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
