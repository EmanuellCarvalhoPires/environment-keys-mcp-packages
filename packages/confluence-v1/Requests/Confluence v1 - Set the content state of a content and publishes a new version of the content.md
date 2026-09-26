---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-states
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: PUT
path: "/wiki/rest/api/content/{id}/state"
category: "Content states"
writes_data: true
tool_note: "[[confluence_v1_set_the_content_state_of_a_content_and_publishes_a]]"
---
# Confluence v1 - Set the content state of a content and publishes a new version of the content

**Set the content state of a content and publishes a new version of the content.** — `PUT /wiki/rest/api/content/{id}/state`

- Run by the tool [[confluence_v1_set_the_content_state_of_a_content_and_publishes_a]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
PUT {{service.url}}/wiki/rest/api/content/{{param:id}}/state?status={{param:status}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The Id of the content whose content state is to be set.
- `status` (query, string, required) — Status of content onto which state will be placed. If draft, then draft state will change. If current, state will be placed onto a new version of the content with same body as previous version.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Sets the content state of the content specified and creates a new version
(publishes the content without changing the body) of the content with the new state.

You may pass in either an id of a state, or the name and color of a desired new state.
If all 3 are passed in, id will be used.
If the name and color passed in already exist under the current user's existing custom states, the existing state will be reused.
If custom states are disabled in the space of the content (which can be determined by getting the content state space settings of the content's space)
then this set will fail.

You may not remove a content state via this PUT request. You must use the DELETE method. A specified state is required in the body of this request.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to edit the content.
