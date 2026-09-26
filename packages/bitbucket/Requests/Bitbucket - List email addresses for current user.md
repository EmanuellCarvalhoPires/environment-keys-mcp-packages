---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/users
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/user/emails"
category: "Users"
writes_data: false
tool_note: "[[bitbucket_list_email_addresses_for_current_user]]"
---
# Bitbucket - List email addresses for current user

**List email addresses for current user** — `GET /user/emails`

- Run by the tool [[bitbucket_list_email_addresses_for_current_user]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/user/emails
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns all the authenticated user's email addresses. Both
confirmed and unconfirmed.
