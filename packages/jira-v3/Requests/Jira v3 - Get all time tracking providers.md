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
path: "/rest/api/3/configuration/timetracking/list"
category: "Time tracking"
writes_data: false
tool_note: "[[jira_get_all_time_tracking_providers]]"
---
# Jira v3 - Get all time tracking providers

**Get all time tracking providers** — `GET /rest/api/3/configuration/timetracking/list`

- Run by the tool [[jira_get_all_time_tracking_providers]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/configuration/timetracking/list
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns all time tracking providers. By default, Jira only has one time tracking provider: *JIRA provided time tracking*. However, you can install other time tracking providers via apps from the Atlassian Marketplace. For more information on time tracking providers, see the documentation for the [ Time Tracking Provider](https://developer.atlassian.com/cloud/jira/platform/modules/time-tracking-provider/) module.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
