---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/app-data-policies
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/data-policy"
category: "App data policies"
writes_data: false
tool_note: "[[jira_get_data_policy_for_the_workspace]]"
---
# Jira v3 - Get data policy for the workspace

**Get data policy for the workspace** — `GET /rest/api/3/data-policy`

- Run by the tool [[jira_get_data_policy_for_the_workspace]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/data-policy
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns data policy for the workspace.
