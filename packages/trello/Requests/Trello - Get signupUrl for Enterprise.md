---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/enterprises
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/enterprises/{id}/signupUrl"
category: "Enterprises"
writes_data: false
---
# Trello - Get signupUrl for Enterprise

**Get signupUrl for Enterprise** — `GET /enterprises/{id}/signupUrl`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get signupUrl for Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/enterprises/{{param:id}}/signupUrl?authenticate={{param:authenticate}}&confirmationAccepted={{param:confirmationAccepted}}&returnUrl={{param:returnUrl}}&tosAccepted={{param:tosAccepted}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the enterprise to retrieve.
- `authenticate` (query, string, optional) — Query parameter authenticate.
- `confirmationAccepted` (query, string, optional) — Query parameter confirmationAccepted.
- `returnUrl` (query, string, optional) — Any valid URL.
- `tosAccepted` (query, string, optional) — Designates whether the user has seen/consented to the Trello ToS prior to being redirected to the enterprise signup page/their IdP.

## Original description

Get the signup URL for an enterprise.
