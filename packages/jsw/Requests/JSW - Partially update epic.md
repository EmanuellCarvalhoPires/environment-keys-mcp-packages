---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/epic
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/agile/1.0/epic/{epicIdOrKey}"
category: "Epic"
writes_data: true
tool_note: "[[jsw_partially_update_epic]]"
---
# JSW - Partially update epic

**Partially update epic** — `POST /rest/agile/1.0/epic/{epicIdOrKey}`

- Run by the tool [[jsw_partially_update_epic]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/agile/1.0/epic/{{param:epicIdOrKey}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `epicIdOrKey` (path, string, required) — The id or key of the epic to update.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "color": {
    "key": "color_6"
  },
  "done": true,
  "name": "epic 2",
  "summary": "epic 2 summary"
}
```

## Original description

Performs a partial update of the epic. A partial update means that fields not present in the request JSON will not be updated. Valid values for color are `color_1` to `color_9`. **Note:** This operation does not work for epics in next-gen projects.
