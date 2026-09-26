---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/sprint
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: PUT
path: "/rest/agile/1.0/sprint/{sprintId}/properties/{propertyKey}"
category: "Sprint"
writes_data: true
tool_note: "[[jsw_set_property]]"
---
# JSW - Set property

**Set property** — `PUT /rest/agile/1.0/sprint/{sprintId}/properties/{propertyKey}`

- Run by the tool [[jsw_set_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
PUT {{service.url}}/rest/agile/1.0/sprint/{{param:sprintId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `sprintId` (path, string, required) — the ID of the sprint on which the property will be set.
- `propertyKey` (path, string, required) — the key of the sprint's property. The maximum length of the key is 255 bytes.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Sets the value of the specified sprint's property.

You can use this resource to store a custom data against the sprint identified by the id. The user who stores the data is required to have permissions to modify the sprint.
