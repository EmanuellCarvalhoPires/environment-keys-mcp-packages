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
path: "/organizations/{id}/prefs/associatedDomain"
category: "Organizations"
writes_data: true
---
# Trello - Remove the associated Google Apps domain from a Workspace

**Remove the associated Google Apps domain from a Workspace** — `DELETE /organizations/{id}/prefs/associatedDomain`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Remove the associated Google Apps domain from a Workspace"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/organizations/{{param:id}}/prefs/associatedDomain
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization

## Original description

Remove the associated Google Apps domain from a Workspace
