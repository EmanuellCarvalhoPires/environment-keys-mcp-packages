---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/epic
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/agile/1.0/epic/{epicIdOrKey}"
category: "Epic"
writes_data: false
tool_note: "[[jsw_get_epic]]"
---
# JSW - Get epic

**Get epic** — `GET /rest/agile/1.0/epic/{epicIdOrKey}`

- Run by the tool [[jsw_get_epic]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/epic/{{param:epicIdOrKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `epicIdOrKey` (path, string, required) — The id or key of the requested epic.

## Original description

Returns the epic for a given epic ID. This epic will only be returned if the user has permission to view it. **Note:** This operation does not work for epics in next-gen projects.
