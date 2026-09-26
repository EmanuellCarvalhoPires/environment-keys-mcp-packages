---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-notification-schemes
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/notificationscheme/{id}"
category: "Issue notification schemes"
writes_data: false
tool_note: "[[jira_get_notification_scheme]]"
---
# Jira v3 - Get notification scheme

**Get notification scheme** — `GET /rest/api/3/notificationscheme/{id}`

- Run by the tool [[jira_get_notification_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/notificationscheme/{{param:id}}?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the notification scheme. Use Get notification schemes paginated to get a list of notification scheme IDs.
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list.

## Original description

Returns a [notification scheme](https://confluence.atlassian.com/x/8YdKLg), including the list of events and the recipients who will receive notifications for those events.

**[Permissions](#permissions) required:** Permission to access Jira, however, the user must have permission to administer at least one project associated with the notification scheme.
