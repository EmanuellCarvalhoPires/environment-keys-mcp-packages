---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/time-tracking
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/configuration/timetracking/options"
category: "Time tracking"
writes_data: false
tool_note: "[[jira_get_time_tracking_settings]]"
---
# Jira v3 - Get time tracking settings

**Get time tracking settings** — `GET /rest/api/3/configuration/timetracking/options`

- Run by the tool [[jira_get_time_tracking_settings]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/configuration/timetracking/options
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the time tracking settings. This includes settings such as the time format, default time unit, and others. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
