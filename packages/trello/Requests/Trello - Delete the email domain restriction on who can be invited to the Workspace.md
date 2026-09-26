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
path: "/organizations/{id}/prefs/orgInviteRestrict"
category: "Organizations"
writes_data: true
---
# Trello - Delete the email domain restriction on who can be invited to the Workspace

**Delete the email domain restriction on who can be invited to the Workspace** — `DELETE /organizations/{id}/prefs/orgInviteRestrict`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete the email domain restriction on who can be invited to the Workspace"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/organizations/{{param:id}}/prefs/orgInviteRestrict
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization

## Original description

Remove the email domain restriction on who can be invited to the Workspace
