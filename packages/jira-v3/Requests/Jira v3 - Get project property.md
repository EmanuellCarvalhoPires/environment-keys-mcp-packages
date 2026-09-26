---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-properties
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}"
category: "Project properties"
writes_data: false
tool_note: "[[jira_get_project_property]]"
---
# Jira v3 - Get project property

**Get project property** — `GET /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}`

- Run by the tool [[jira_get_project_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).
- `propertyKey` (path, string, required) — The project property key. Use Get project property keys to get a list of all project property keys.

## Original description

Returns the value of a [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the property.
