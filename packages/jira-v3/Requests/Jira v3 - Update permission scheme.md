---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/permission-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/permissionscheme/{schemeId}"
category: "Permission schemes"
writes_data: true
tool_note: "[[jira_update_permission_scheme]]"
---
# Jira v3 - Update permission scheme

**Update permission scheme** — `PUT /rest/api/3/permissionscheme/{schemeId}`

- Run by the tool [[jira_update_permission_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/permissionscheme/{{param:schemeId}}?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `schemeId` (path, string, required) — The ID of the permission scheme to update.
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "description",
  "name": "Example permission scheme",
  "permissions": [
    {
      "holder": {
        "parameter": "jira-core-users",
        "type": "group",
        "value": "ca85fac0-d974-40ca-a615-7af99c48d24f"
      },
      "permission": "ADMINISTER_PROJECTS"
    }
  ]
}
```

## Original description

Updates a permission scheme. Below are some important things to note when using this resource:

 *  If a permissions list is present in the request, then it is set in the permission scheme, overwriting *all existing* grants.
 *  If you want to update only the name and description, then do not send a permissions list in the request.
 *  Sending an empty list will remove all permission grants from the permission scheme.

If you want to add or delete a permission grant instead of updating the whole list, see [Create permission grant](#api-rest-api-3-permissionscheme-schemeId-permission-post) or [Delete permission scheme entity](#api-rest-api-3-permissionscheme-schemeId-permission-permissionId-delete).

See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-and-grants) for more details.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
