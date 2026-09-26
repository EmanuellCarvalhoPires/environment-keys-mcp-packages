---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-priorities
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/priority/default"
category: "Issue priorities"
writes_data: true
tool_note: "[[jira_set_default_priority]]"
---
# Jira v3 - Set default priority

**Set default priority** — `PUT /rest/api/3/priority/default`

- Run by the tool [[jira_set_default_priority]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/priority/default
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "id": "3"
}
```

## Original description

Sets default issue priority.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
