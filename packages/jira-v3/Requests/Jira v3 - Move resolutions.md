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
path: "/rest/api/3/resolution/move"
category: "Issue resolutions"
writes_data: true
tool_note: "[[jira_move_resolutions]]"
---
# Jira v3 - Move resolutions

**Move resolutions** — `PUT /rest/api/3/resolution/move`

- Run by the tool [[jira_move_resolutions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/resolution/move
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "after": "10002",
  "ids": [
    "10000",
    "10001"
  ]
}
```

## Original description

Changes the order of issue resolutions.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
