---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/users
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/user/emails/{email}"
category: "Users"
writes_data: false
tool_note: "[[bitbucket_get_an_email_address_for_current_user]]"
---
# Bitbucket - Get an email address for current user

**Get an email address for current user** — `GET /user/emails/{email}`

- Run by the tool [[bitbucket_get_an_email_address_for_current_user]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/user/emails/{{param:email}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `email` (path, string, required) — Value of email in the path.

## Original description

Returns details about a specific one of the authenticated user's
email addresses.

Details describe whether the address has been confirmed by the user and
whether it is the user's primary address or not.
