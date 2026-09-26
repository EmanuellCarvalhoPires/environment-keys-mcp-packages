---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/organizations
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/organizations/{id}/tags/{idTag}"
category: "Organizations"
writes_data: true
---
# Trello - Delete an Organization's Tag

**Delete an Organization's Tag** — `DELETE /organizations/{id}/tags/{idTag}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete an Organization's Tag"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/organizations/{{param:id}}/tags/{{param:idTag}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization
- `idTag` (path, string, required) — The ID of the tag to delete

## Original description

Delete an organization's tag
