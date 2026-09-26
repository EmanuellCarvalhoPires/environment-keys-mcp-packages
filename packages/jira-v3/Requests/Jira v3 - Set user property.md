---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/user-properties
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/user/properties/{propertyKey}"
category: "User properties"
writes_data: true
tool_note: "[[jira_set_user_property]]"
---
# Jira v3 - Set user property

**Set user property** — `PUT /rest/api/3/user/properties/{propertyKey}`

- Run by the tool [[jira_set_user_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/user/properties/{{param:propertyKey}}?accountId={{param:accountId}}&userKey={{param:userKey}}&username={{param:username}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `propertyKey` (path, string, required) — The key of the user's property. The maximum length is 255 characters.
- `accountId` (query, string, optional) — The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5.
- `userKey` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. See the deprecation notice for details.
- `username` (query, string, optional) — This parameter is no longer available and will be removed from the documentation soon. See the deprecation notice for details.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Sets the value of a user's property. Use this resource to store custom data against a user.

Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set a property on any user.
 *  Access to Jira, to set a property on the calling user's record.
