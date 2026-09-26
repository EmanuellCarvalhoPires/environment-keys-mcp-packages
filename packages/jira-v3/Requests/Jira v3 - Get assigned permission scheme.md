---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-permission-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectKeyOrId}/permissionscheme"
category: "Project permission schemes"
writes_data: false
tool_note: "[[jira_get_assigned_permission_scheme]]"
---
# Jira v3 - Get assigned permission scheme

**Get assigned permission scheme** — `GET /rest/api/3/project/{projectKeyOrId}/permissionscheme`

- Run by the tool [[jira_get_assigned_permission_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectKeyOrId}}/permissionscheme?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectKeyOrId` (path, string, required) — The project ID or project key (case sensitive).
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value.

## Original description

Gets the [permission scheme](https://confluence.atlassian.com/x/yodKLg) associated with the project.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).
