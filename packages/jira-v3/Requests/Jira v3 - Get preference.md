---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/myself
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/mypreferences"
category: "Myself"
writes_data: false
tool_note: "[[jira_get_preference]]"
---
# Jira v3 - Get preference

**Get preference** — `GET /rest/api/3/mypreferences`

- Run by the tool [[jira_get_preference]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/mypreferences?key={{param:key}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `key` (query, string, required) — The key of the preference.

## Original description

Returns the value of a preference of the current user.

Note that these keys are deprecated:

 *  *jira.user.locale* The locale of the user. By default this is not set and the user takes the locale of the instance.
 *  *jira.user.timezone* The time zone of the user. By default this is not set and the user takes the timezone of the instance.

These system preferences keys will be deprecated by 15/07/2024. You can still retrieve these keys, but it will not have any impact on Notification behaviour.

 *  *user.notifications.watcher* Whether the user gets notified when they are watcher.
 *  *user.notifications.assignee* Whether the user gets notified when they are assignee.
 *  *user.notifications.reporter* Whether the user gets notified when they are reporter.
 *  *user.notifications.mentions* Whether the user gets notified when they are mentions.

Use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API to manage timezone and locale instead.

**[Permissions](#permissions) required:** Permission to access Jira.
