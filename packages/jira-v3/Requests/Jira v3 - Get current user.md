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
path: "/rest/api/3/myself"
category: "Myself"
writes_data: false
tool_note: "[[jira_get_current_user]]"
---
# Jira v3 - Get current user

**Get current user** — `GET /rest/api/3/myself`

- Run by the tool [[jira_get_current_user]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/myself?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `expand` (query, string, optional) — Use expand to include additional information about user in the response. This parameter accepts a comma-separated list.

## Original description

Returns details for the current user.

**[Permissions](#permissions) required:** Permission to access Jira.
