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
path: "/wiki/rest/api/space/{spaceKey}/state/content"
category: "Content states"
writes_data: false
tool_note: "[[confluence_v1_get_content_in_space_with_given_content_state]]"
---
# Confluence v1 - Get content in space with given content state

**Get content in space with given content state** — `GET /wiki/rest/api/space/{spaceKey}/state/content`

- Run by the tool [[confluence_v1_get_content_in_space_with_given_content_state]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/space/{{param:spaceKey}}/state/content?state-id={{param:state_id}}&expand={{param:expand}}&limit={{param:limit}}&start={{param:start}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `spaceKey` (path, string, required) — The key of the space to be queried for its content state settings.
- `state_id` (query, string, required) — The id of the content state to filter content by
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the content to expand. Options include: space, version, history, children, etc. Ex: space,version
- `limit` (query, string, optional) — Maximum number of results to return
- `start` (query, string, optional) — Number of result to start returning. (0 indexed)

## Original description

Returns all content that has the provided content state in a space.

If the expand query parameter is used with the `body.export_view` and/or `body.styled_view` properties, then the query limit parameter will be restricted to a maximum value of 25.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'View' permission for the space.
