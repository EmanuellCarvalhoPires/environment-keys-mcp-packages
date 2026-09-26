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
path: "/rest/api/3/notificationscheme/{id}/notification"
category: "Issue notification schemes"
writes_data: true
tool_note: "[[jira_add_notifications_to_notification_scheme]]"
---
# Jira v3 - Add notifications to notification scheme

**Add notifications to notification scheme** — `PUT /rest/api/3/notificationscheme/{id}/notification`

- Run by the tool [[jira_add_notifications_to_notification_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/notificationscheme/{{param:id}}/notification
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

Adds notifications to a notification scheme. You can add up to 1000 notifications per request.

*Deprecated: The notification type `EmailAddress` is no longer supported in Cloud. Refer to the [changelog](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-1031) for more details.*

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
