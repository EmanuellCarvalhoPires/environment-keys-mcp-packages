---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/myself
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/mypreferences"
category: "Myself"
writes_data: true
tool_note: "[[jira_delete_preference]]"
---
# Jira v3 - Delete preference

**Delete preference** — `DELETE /rest/api/3/mypreferences`

- Run by the tool [[jira_delete_preference]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/mypreferences?key={{param:key}}
Authorization: {{service.auth_token}}
```

## Parameters

- `key` (query, string, required) — The key of the preference.

## Original description

Deletes a preference of the user, which restores the default value of system defined settings.

Note that these keys are deprecated:

 *  *jira.user.locale* The locale of the user. By default, not set. The user takes the instance locale.
 *  *jira.user.timezone* The time zone of the user. By default, not set. The user takes the instance timezone.

Use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API to manage timezone and locale instead.

**[Permissions](#permissions) required:** Permission to access Jira.
