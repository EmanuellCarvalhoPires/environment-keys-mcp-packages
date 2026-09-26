---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/myself
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/mypreferences"
category: "Myself"
writes_data: true
tool_note: "[[jira_set_preference]]"
---
# Jira v3 - Set preference

**Set preference** — `PUT /rest/api/3/mypreferences`

- Run by the tool [[jira_set_preference]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/mypreferences?key={{param:key}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `key` (query, string, required) — The key of the preference. The maximum length is 255 characters.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a preference for the user or updates a preference's value by sending a plain text string. For example, `false`. An arbitrary preference can be created with the value containing up to 255 characters. In addition, the following keys define system preferences that can be set or created:

 *  *user.notifications.mimetype* The mime type used in notifications sent to the user. Defaults to `html`.
 *  *user.default.share.private* Whether new [ filters](https://confluence.atlassian.com/x/eQiiLQ) are set to private. Defaults to `true`.
 *  *user.keyboard.shortcuts.disabled* Whether keyboard shortcuts are disabled. Defaults to `false`.
 *  *user.autowatch.disabled* Whether the user automatically watches issues they create or add a comment to. By default, not set: the user takes the instance autowatch setting.
 *  *user.notifiy.own.changes* Whether the user gets notified of their own changes.

Note that these keys are deprecated:

 *  *jira.user.locale* The locale of the user. By default, not set. The user takes the instance locale.
 *  *jira.user.timezone* The time zone of the user. By default, not set. The user takes the instance timezone.

These system preferences keys will be deprecated by 15/07/2024. You can still use these keys to create arbitrary preferences, but it will not have any impact on Notification behaviour.

 *  *user.notifications.watcher* Whether the user gets notified when they are watcher.
 *  *user.notifications.assignee* Whether the user gets notified when they are assignee.
 *  *user.notifications.reporter* Whether the user gets notified when they are reporter.
 *  *user.notifications.mentions* Whether the user gets notified when they are mentions.

Use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API to manage timezone and locale instead.

**[Permissions](#permissions) required:** Permission to access Jira.
