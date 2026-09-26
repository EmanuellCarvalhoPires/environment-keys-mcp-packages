---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-properties
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/user/properties"
category: "User properties"
writes_data: false
tool_note: "[[jira_get_user_property_keys]]"
---
# Jira v3 - Get user property keys

**Get user property keys** — `GET /rest/api/3/user/properties`

- Run by the tool [[jira_get_user_property_keys]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/user/properties?accountId={{param:accountId}}&userKey={{param:userKey}}&username={{param:username}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `accountId` (query, string, optional) — The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5.
- `userKey` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. See the deprecation notice for details.
- `username` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. See the deprecation notice for details.

## Original description

Returns the keys of all properties for a user.

Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to access the property keys on any user.
 *  Access to Jira, to access the calling user's property keys.
