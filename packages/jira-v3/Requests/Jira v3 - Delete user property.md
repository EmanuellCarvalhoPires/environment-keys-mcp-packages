---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-properties
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/user/properties/{propertyKey}"
category: "User properties"
writes_data: true
tool_note: "[[jira_delete_user_property]]"
---
# Jira v3 - Delete user property

**Delete user property** — `DELETE /rest/api/3/user/properties/{propertyKey}`

- Run by the tool [[jira_delete_user_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/user/properties/{{param:propertyKey}}?accountId={{param:accountId}}&userKey={{param:userKey}}&username={{param:username}}
Authorization: {{service.auth_token}}
```

## Parameters

- `propertyKey` (path, string, required) — The key of the user's property.
- `accountId` (query, string, optional) — The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5.
- `userKey` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. See the deprecation notice for details.
- `username` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. See the deprecation notice for details.

## Original description

Deletes a property from a user.

Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to delete a property from any user.
 *  Access to Jira, to delete a property from the calling user's record.
