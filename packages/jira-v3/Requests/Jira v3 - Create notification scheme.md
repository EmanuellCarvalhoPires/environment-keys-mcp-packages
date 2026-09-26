---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-notification-schemes
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/notificationscheme"
category: "Issue notification schemes"
writes_data: true
tool_note: "[[jira_create_notification_scheme]]"
---
# Jira v3 - Create notification scheme

**Create notification scheme** — `POST /rest/api/3/notificationscheme`

- Run by the tool [[jira_create_notification_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/notificationscheme
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "My new scheme description",
  "name": "My new notification scheme",
  "notificationSchemeEvents": [
    {
      "event": {
        "id": "1"
      },
      "notifications": [
        {
          "notificationType": "Group",
          "parameter": "jira-administrators"
        }
      ]
    }
  ]
}
```

## Original description

Creates a notification scheme with notifications. You can create up to 1000 notifications per request.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
