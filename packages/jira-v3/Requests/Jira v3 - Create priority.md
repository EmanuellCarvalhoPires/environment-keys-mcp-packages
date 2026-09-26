---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-priorities
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/priority"
category: "Issue priorities"
writes_data: true
tool_note: "[[jira_create_priority]]"
---
# Jira v3 - Create priority

**Create priority** — `POST /rest/api/3/priority`

- Run by the tool [[jira_create_priority]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/priority
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "My priority description",
  "iconUrl": "/images/icons/priorities/major.png",
  "name": "My new priority",
  "statusColor": "#ABCDEF"
}
```

## Original description

Creates an issue priority.

**Deprecation notice:** The `iconUrl` parameter was sunset on 16th Mar 2025, and replaced with `avatarId`. See [CHANGE-1525](https://developer.atlassian.com/changelog/#CHANGE-1525).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
