---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/tokens
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/tokens/{token}/"
category: "Tokens"
writes_data: true
---
# Trello - Delete a Token

**Delete a Token** — `DELETE /tokens/{token}/`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete a Token"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/tokens/{{param:token}}/
Authorization: {{service.auth_token}}
```

## Parameters

- `token` (path, string, required) — Value of token in the path.

## Original description

Delete a token.
