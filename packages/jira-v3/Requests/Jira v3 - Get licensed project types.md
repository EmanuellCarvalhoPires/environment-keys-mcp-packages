---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-types
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/type/accessible"
category: "Project types"
writes_data: false
tool_note: "[[jira_get_licensed_project_types]]"
---
# Jira v3 - Get licensed project types

**Get licensed project types** — `GET /rest/api/3/project/type/accessible`

- Run by the tool [[jira_get_licensed_project_types]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/type/accessible
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns all [project types](https://confluence.atlassian.com/x/Var1Nw) with a valid license.
