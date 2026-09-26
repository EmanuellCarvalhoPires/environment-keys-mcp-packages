---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-notification-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/notificationscheme/{id}"
category: "Issue notification schemes"
writes_data: true
tool_note: "[[jira_update_notification_scheme]]"
---
# Jira v3 - Update notification scheme

**Update notification scheme** — `PUT /rest/api/3/notificationscheme/{id}`

- Run by the tool [[jira_update_notification_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/notificationscheme/{{param:id}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the notification scheme.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "My updated notification scheme description",
  "name": "My updated notification scheme"
}
```

## Original description

Updates a notification scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
