---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/users
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/user/bulk"
category: "Users"
writes_data: false
tool_note: "[[confluence_v1_get_multiple_users_using_ids]]"
---
# Confluence v1 - Get multiple users using ids

**Get multiple users using ids** — `GET /wiki/rest/api/user/bulk`

- Run by the tool [[confluence_v1_get_multiple_users_using_ids]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/user/bulk?accountId={{param:accountId}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `accountId` (query, string, required) — A list of accountId's of users to be returned.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the user to expand. - operations returns the operations that the user is allowed to do.

## Original description

Returns user details for the ids provided in the request.
Currently this API returns a maximum of 100 results.
If more than 100 account ids are passed in, then the first 100 will be returned.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
