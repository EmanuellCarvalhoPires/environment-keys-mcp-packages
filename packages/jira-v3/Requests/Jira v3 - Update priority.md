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
path: "/rest/api/3/priority/{id}"
category: "Issue priorities"
writes_data: true
tool_note: "[[jira_update_priority]]"
---
# Jira v3 - Update priority

**Update priority** — `PUT /rest/api/3/priority/{id}`

- Run by the tool [[jira_update_priority]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/priority/{{param:id}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the issue priority.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "My updated priority description",
  "iconUrl": "/images/icons/priorities/minor.png",
  "name": "My updated priority",
  "statusColor": "#123456"
}
```

## Original description

Updates an issue priority.

At least one request body parameter must be defined.

**Deprecation notice:** The `iconUrl` parameter was sunset on 16th Mar 2025, and replaced with `avatarId`. See [CHANGE-1525](https://developer.atlassian.com/changelog/#CHANGE-1525).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
