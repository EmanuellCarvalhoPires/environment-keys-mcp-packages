---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-types
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issuetype/{id}"
category: "Issue types"
writes_data: true
tool_note: "[[jira_update_issue_type]]"
---
# Jira v3 - Update issue type

**Update issue type** — `PUT /rest/api/3/issuetype/{id}`

- Run by the tool [[jira_update_issue_type]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issuetype/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the issue type.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "avatarId": 1,
  "description": "description",
  "name": "name"
}
```

## Original description

Updates the issue type.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
