---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/events"
category: "Issues"
writes_data: false
tool_note: "[[jira_get_events]]"
---
# Jira v3 - Get events

**Get events** — `GET /rest/api/3/events`

- Run by the tool [[jira_get_events]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/events
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns all issue events.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
