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
path: "/rest/api/3/data-policy/project"
category: "App data policies"
writes_data: false
tool_note: "[[jira_get_data_policy_for_projects]]"
---
# Jira v3 - Get data policy for projects

**Get data policy for projects** — `GET /rest/api/3/data-policy/project`

- Run by the tool [[jira_get_data_policy_for_projects]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/data-policy/project?ids={{param:ids}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `ids` (query, string, optional) — A list of project identifiers. This parameter accepts a comma-separated list.

## Original description

Returns data policies for the projects specified in the request.
