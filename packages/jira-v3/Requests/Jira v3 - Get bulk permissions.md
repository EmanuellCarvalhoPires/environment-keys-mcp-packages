---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/permissions
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/permissions/check"
category: "Permissions"
writes_data: false
tool_note: "[[jira_get_bulk_permissions]]"
---
# Jira v3 - Get bulk permissions

**Get bulk permissions** — `POST /rest/api/3/permissions/check`

- Run by the tool [[jira_get_bulk_permissions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/permissions/check
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "accountId": "5b10a2844c20165700ede21g",
  "globalPermissions": [
    "ADMINISTER"
  ],
  "projectPermissions": [
    {
      "issues": [
        10010,
        10011,
        10012,
        10013,
        10014
      ],
      "permissions": [
        "EDIT_ISSUES"
      ],
      "projects": [
        10001
      ]
    }
  ]
}
```

## Original description

Returns:

 *  for a list of global permissions, the global permissions granted to a user.
 *  for a list of project permissions and lists of projects and issues, for each project permission a list of the projects and issues a user can access or manipulate.

If no account ID is provided, the operation returns details for the logged in user.

Note that:

 *  Invalid project and issue IDs are ignored.
 *  A maximum of 1000 projects and 1000 issues can be checked.
 *  Null values in `globalPermissions`, `projectPermissions`, `projectPermissions.projects`, and `projectPermissions.issues` are ignored.
 *  Empty strings in `projectPermissions.permissions` are ignored.

**Deprecation notice:** The required OAuth 2.0 scopes will be updated on June 15, 2024.

 *  **Classic**: `read:jira-work`
 *  **Granular**: `read:permission:jira`

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to check the permissions for other users, otherwise none. However, Connect apps can make a call from the app server to the product to obtain permission details for any user, without admin permission. This Connect app ability doesn't apply to calls made using AP.request() in a browser.
