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
path: "/wiki/rest/api/content/{id}/state/available"
category: "Content states"
writes_data: false
tool_note: "[[confluence_v1_gets_available_content_states_for_content]]"
---
# Confluence v1 - Gets available content states for content

**Gets available content states for content.** — `GET /wiki/rest/api/content/{id}/state/available`

- Run by the tool [[confluence_v1_gets_available_content_states_for_content]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/content/{{param:id}}/state/available
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — id of content to get available states for

## Original description

Gets content states that are available for the content to be set as.
Will return all enabled Space Content States.
Will only return most the 3 most recently published custom content states to match UI editor list.
To get all custom content states, use the /content-states endpoint.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to edit the content.
