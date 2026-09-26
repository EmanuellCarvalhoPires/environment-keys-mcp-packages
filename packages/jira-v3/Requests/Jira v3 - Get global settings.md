---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/jira-settings
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/configuration"
category: "Jira settings"
writes_data: false
tool_note: "[[jira_get_global_settings]]"
---
# Jira v3 - Get global settings

**Get global settings** — `GET /rest/api/3/configuration`

- Run by the tool [[jira_get_global_settings]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/configuration
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the [global settings](https://confluence.atlassian.com/x/qYXKM) in Jira. These settings determine whether optional features (for example, subtasks, time tracking, and others) are enabled. If time tracking is enabled, this operation also returns the time tracking configuration.

**[Permissions](#permissions) required:** Permission to access Jira.
