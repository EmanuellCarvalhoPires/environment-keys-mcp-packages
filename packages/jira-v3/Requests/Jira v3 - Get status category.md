---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-status-categories
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/statuscategory/{idOrKey}"
category: "Workflow status categories"
writes_data: false
tool_note: "[[jira_get_status_category]]"
---
# Jira v3 - Get status category

**Get status category** — `GET /rest/api/3/statuscategory/{idOrKey}`

- Run by the tool [[jira_get_status_category]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/statuscategory/{{param:idOrKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `idOrKey` (path, string, required) — The ID or key of the status category.

## Original description

Returns a status category. Status categories provided a mechanism for categorizing [statuses](#api-rest-api-3-status-idOrName-get).

**[Permissions](#permissions) required:** Permission to access Jira.
