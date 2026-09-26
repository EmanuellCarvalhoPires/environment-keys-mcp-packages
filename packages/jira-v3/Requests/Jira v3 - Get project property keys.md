---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-properties
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectIdOrKey}/properties"
category: "Project properties"
writes_data: false
tool_note: "[[jira_get_project_property_keys]]"
---
# Jira v3 - Get project property keys

**Get project property keys** — `GET /rest/api/3/project/{projectIdOrKey}/properties`

- Run by the tool [[jira_get_project_property_keys]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/properties
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).

## Original description

Returns all [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) keys for the project.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
