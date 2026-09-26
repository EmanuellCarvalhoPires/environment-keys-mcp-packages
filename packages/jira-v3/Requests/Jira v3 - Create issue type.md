---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-types
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issuetype"
category: "Issue types"
writes_data: true
tool_note: "[[jira_create_issue_type]]"
---
# Jira v3 - Create issue type

**Create issue type** — `POST /rest/api/3/issuetype`

- Run by the tool [[jira_create_issue_type]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issuetype
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "description",
  "name": "name",
  "type": "standard"
}
```

## Original description

Creates an issue type.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
