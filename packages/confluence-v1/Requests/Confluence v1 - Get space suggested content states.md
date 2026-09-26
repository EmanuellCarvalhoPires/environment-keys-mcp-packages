---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-states
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/space/{spaceKey}/state"
category: "Content states"
writes_data: false
tool_note: "[[confluence_v1_get_space_suggested_content_states]]"
---
# Confluence v1 - Get space suggested content states

**Get space suggested content states** — `GET /wiki/rest/api/space/{spaceKey}/state`

- Run by the tool [[confluence_v1_get_space_suggested_content_states]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}/state
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to be queried for its content state settings.

## Original description

Get content states that are suggested in the space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'View' permission for the space.
