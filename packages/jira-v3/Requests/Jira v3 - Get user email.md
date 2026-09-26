---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/users
  - api/operation/list
  - api/effect/read
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/user/email"
category: "Users"
writes_data: false
---
# Jira v3 - Get user email

**Get user email** — `GET /rest/api/3/user/email`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Jira v3 - Get user email"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/user/email?accountId={{param:accountId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `accountId` (query, string, required) — The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5.

## Original description

Returns a user's email address regardless of the user's profile visibility settings. For Connect apps, this API is only available to apps approved by Atlassian, according to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-to-email-address/27603). For Forge apps, this API only supports access via asApp() requests.
