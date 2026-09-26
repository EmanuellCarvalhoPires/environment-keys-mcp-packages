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
path: "/rest/api/3/configuration/timetracking"
category: "Time tracking"
writes_data: false
tool_note: "[[jira_get_selected_time_tracking_provider]]"
---
# Jira v3 - Get selected time tracking provider

**Get selected time tracking provider** — `GET /rest/api/3/configuration/timetracking`

- Run by the tool [[jira_get_selected_time_tracking_provider]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/configuration/timetracking
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the time tracking provider that is currently selected. Note that if time tracking is disabled, then a successful but empty response is returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
