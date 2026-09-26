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
path: "/wiki/rest/api/content-states"
category: "Content states"
writes_data: false
tool_note: "[[confluence_v1_get_custom_content_states]]"
---
# Confluence v1 - Get Custom Content States

**Get Custom Content States** — `GET /wiki/rest/api/content-states`

- Run by the tool [[confluence_v1_get_custom_content_states]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/content-states
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Get custom content states that authenticated user has created.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**
Must have user authentication.
