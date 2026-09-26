---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/agile/1.0/sprint/{sprintId}/properties/{propertyKey}"
category: "Sprint"
writes_data: false
tool_note: "[[jsw_get_property]]"
---
# JSW - Get property

**Get property** — `GET /rest/agile/1.0/sprint/{sprintId}/properties/{propertyKey}`

- Run by the tool [[jsw_get_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/sprint/{{param:sprintId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `sprintId` (path, string, required) — the ID of the sprint from which the property will be returned.
- `propertyKey` (path, string, required) — the key of the property to return.

## Original description

Returns the value of the property with a given key from the sprint identified by the provided id. The user who retrieves the property is required to have permissions to view the sprint.
