---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/time-tracking
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/configuration/timetracking/options"
category: "Time tracking"
writes_data: true
tool_note: "[[jira_set_time_tracking_settings]]"
---
# Jira v3 - Set time tracking settings

**Set time tracking settings** — `PUT /rest/api/3/configuration/timetracking/options`

- Run by the tool [[jira_set_time_tracking_settings]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/configuration/timetracking/options
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "defaultUnit": "hour",
  "timeFormat": "pretty",
  "workingDaysPerWeek": 5.5,
  "workingHoursPerDay": 7.6
}
```

## Original description

Sets the time tracking settings.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
