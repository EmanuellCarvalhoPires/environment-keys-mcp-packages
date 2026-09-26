---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-status-categories
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/statuscategory"
category: "Workflow status categories"
writes_data: false
tool_note: "[[jira_get_all_status_categories]]"
---
# Jira v3 - Get all status categories

**Get all status categories** — `GET /rest/api/3/statuscategory`

- Run by the tool [[jira_get_all_status_categories]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/statuscategory
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns a list of all status categories.

**[Permissions](#permissions) required:** Permission to access Jira.
