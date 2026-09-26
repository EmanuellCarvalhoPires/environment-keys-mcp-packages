---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-resolutions
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/resolution/{id}"
category: "Issue resolutions"
writes_data: true
tool_note: "[[jira_update_resolution]]"
---
# Jira v3 - Update resolution

**Update resolution** — `PUT /rest/api/3/resolution/{id}`

- Run by the tool [[jira_update_resolution]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/resolution/{{param:id}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the issue resolution.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "My updated resolution description",
  "name": "My updated resolution"
}
```

## Original description

Updates an issue resolution.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
