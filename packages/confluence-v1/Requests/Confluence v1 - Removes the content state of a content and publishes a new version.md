---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-states
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: DELETE
path: "/wiki/rest/api/content/{id}/state"
category: "Content states"
writes_data: true
tool_note: "[[confluence_v1_removes_the_content_state_of_a_content_and_publish]]"
---
# Confluence v1 - Removes the content state of a content and publishes a new version

**Removes the content state of a content and publishes a new version.** — `DELETE /wiki/rest/api/content/{id}/state`

- Run by the tool [[confluence_v1_removes_the_content_state_of_a_content_and_publish]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
DELETE {{service.url}}/wiki/rest/api/content/{{param:id}}/state?status={{param:status}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The Id of the content whose content state is to be set.
- `status` (query, string, optional) — status of content state from which to delete state. Can be draft or archived

## Original description

Removes the content state of the content specified and creates a new version
(publishes the content without changing the body) of the content with the new status.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to edit the content.
