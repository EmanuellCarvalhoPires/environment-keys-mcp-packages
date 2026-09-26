---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: DELETE
path: "/rest/agile/1.0/sprint/{sprintId}/properties/{propertyKey}"
category: "Sprint"
writes_data: true
tool_note: "[[jsw_delete_property]]"
---
# JSW - Delete property

**Delete property** — `DELETE /rest/agile/1.0/sprint/{sprintId}/properties/{propertyKey}`

- Run by the tool [[jsw_delete_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/agile/1.0/sprint/{{param:sprintId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `sprintId` (path, string, required) — the ID of the sprint from which the property will be removed.
- `propertyKey` (path, string, required) — the key of the property to remove.

## Original description

Removes the property from the sprint identified by the id. Ths user removing the property is required to have permissions to modify the sprint.
