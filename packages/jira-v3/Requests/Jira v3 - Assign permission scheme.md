---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-permission-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/project/{projectKeyOrId}/permissionscheme"
category: "Project permission schemes"
writes_data: true
tool_note: "[[jira_assign_permission_scheme]]"
---
# Jira v3 - Assign permission scheme

**Assign permission scheme** — `PUT /rest/api/3/project/{projectKeyOrId}/permissionscheme`

- Run by the tool [[jira_assign_permission_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/project/{{param:projectKeyOrId}}/permissionscheme?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `projectKeyOrId` (path, string, required) — The project ID or project key (case sensitive).
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "id": 10000
}
```

## Original description

Assigns a permission scheme with a project. See [Managing project permissions](https://confluence.atlassian.com/x/yodKLg) for more information about permission schemes.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg)
