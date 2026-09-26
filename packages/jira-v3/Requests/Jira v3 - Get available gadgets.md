---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/dashboard/gadgets"
category: "Dashboards"
writes_data: false
tool_note: "[[jira_get_available_gadgets]]"
---
# Jira v3 - Get available gadgets

**Get available gadgets** — `GET /rest/api/3/dashboard/gadgets`

- Run by the tool [[jira_get_available_gadgets]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/dashboard/gadgets
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Gets a list of all available gadgets that can be added to all dashboards.

**[Permissions](#permissions) required:** None.
