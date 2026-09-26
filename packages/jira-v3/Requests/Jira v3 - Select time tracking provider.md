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
path: "/rest/api/3/configuration/timetracking"
category: "Time tracking"
writes_data: true
tool_note: "[[jira_select_time_tracking_provider]]"
---
# Jira v3 - Select time tracking provider

**Select time tracking provider** — `PUT /rest/api/3/configuration/timetracking`

- Run by the tool [[jira_select_time_tracking_provider]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/configuration/timetracking
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "key": "Jira"
}
```

## Original description

Selects a time tracking provider.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
