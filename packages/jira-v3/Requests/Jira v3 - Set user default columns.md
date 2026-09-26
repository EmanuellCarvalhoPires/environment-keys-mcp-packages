---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/users
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/format/multipart
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/user/columns"
category: "Users"
writes_data: true
---
# Jira v3 - Set user default columns

**Set user default columns** — `PUT /rest/api/3/user/columns`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Set user default columns"`.
- **Format:** the endpoint expects `multipart/form-data` (file upload), which the plugin `http` block cannot build. Kept as reference.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/user/columns?accountId={{param:accountId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `accountId` (query, string, optional) — The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5.

## Original description

Sets the default [ issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user. If an account ID is not passed, the calling user's default columns are set. If no column details are sent, then all default columns are removed.

The parameters for this resource are expressed as HTML form data. For example, in curl:

`curl -X PUT -d columns=summary -d columns=description https://your-domain.atlassian.net/rest/api/3/user/columns?accountId=5b10ac8d82e05b22cc7d4ef5'`

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set the columns on any user.
 *  Permission to access Jira, to set the calling user's columns.
