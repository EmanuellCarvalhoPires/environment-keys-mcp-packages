---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-features
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectIdOrKey}/features"
category: "Project features"
writes_data: false
tool_note: "[[jira_get_project_features]]"
---
# Jira v3 - Get project features

**Get project features** — `GET /rest/api/3/project/{projectIdOrKey}/features`

- Run by the tool [[jira_get_project_features]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/features
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The ID or (case-sensitive) key of the project.

## Original description

Returns the list of features for a project.
