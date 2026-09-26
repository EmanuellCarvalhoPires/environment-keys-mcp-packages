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
path: "/wiki/rest/api/content/{id}/state"
category: "Content states"
writes_data: false
tool_note: "[[confluence_v1_get_content_state]]"
---
# Confluence v1 - Get content state

**Get content state** — `GET /wiki/rest/api/content/{id}/state`

- Run by the tool [[confluence_v1_get_content_state]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/content/{{param:id}}/state?status={{param:status}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The id of the content whose content state is of interest.
- `status` (query, string, optional) — Set status to one of [current,draft,archived]. Default value is current.

## Original description

Gets the current content state of the draft or current version of content. To specify the draft version, set
the parameter status to draft, otherwise archived or current will get the relevant published state.
**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content.
