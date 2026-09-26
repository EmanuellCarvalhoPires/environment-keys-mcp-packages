---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/agile/1.0/sprint/{sprintId}/properties"
category: "Sprint"
writes_data: false
tool_note: "[[jsw_get_properties_keys]]"
---
# JSW - Get properties keys

**Get properties keys** — `GET /rest/agile/1.0/sprint/{sprintId}/properties`

- Run by the tool [[jsw_get_properties_keys]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/sprint/{{param:sprintId}}/properties
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `sprintId` (path, string, required) — the ID of the sprint from which property keys will be returned.

## Original description

Returns the keys of all properties for the sprint identified by the id. The user who retrieves the property keys is required to have permissions to view the sprint.
