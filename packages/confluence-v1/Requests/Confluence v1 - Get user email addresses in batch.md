---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/users
  - api/operation/list
  - api/effect/read
  - api/version/v1
  - api/restriction/app-connect
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/user/email/bulk"
category: "Users"
writes_data: false
---
# Confluence v1 - Get user email addresses in batch

**Get user email addresses in batch** — `GET /wiki/rest/api/user/email/bulk`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Confluence v1 - Get user email addresses in batch"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/user/email/bulk?accountId={{param:accountId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `accountId` (query, string, required) — The account IDs of the users.

## Original description

Returns a user's email address regardless of the user’s profile visibility settings. For Connect apps, this API is only available to apps approved by
Atlassian, according to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-to-email-address/27603).
For Forge apps, this API only supports access via asApp() requests.

Any accounts which are not available will not be included in the result.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
