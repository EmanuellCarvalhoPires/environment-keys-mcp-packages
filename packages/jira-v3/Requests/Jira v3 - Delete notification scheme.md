---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-notification-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/notificationscheme/{notificationSchemeId}"
category: "Issue notification schemes"
writes_data: true
tool_note: "[[jira_delete_notification_scheme]]"
---
# Jira v3 - Delete notification scheme

**Delete notification scheme** — `DELETE /rest/api/3/notificationscheme/{notificationSchemeId}`

- Run by the tool [[jira_delete_notification_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/notificationscheme/{{param:notificationSchemeId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `notificationSchemeId` (path, string, required) — The ID of the notification scheme.

## Original description

Deletes a notification scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
