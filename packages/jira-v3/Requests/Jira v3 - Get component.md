---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-components
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/component/{id}"
category: "Project components"
writes_data: false
tool_note: "[[jira_get_component]]"
---
# Jira v3 - Get component

**Get component** — `GET /rest/api/3/component/{id}`

- Run by the tool [[jira_get_component]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/component/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the component.

## Original description

Returns a component.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for project containing the component.
