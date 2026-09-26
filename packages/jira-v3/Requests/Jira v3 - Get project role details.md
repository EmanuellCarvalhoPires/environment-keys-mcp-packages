---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-roles
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectIdOrKey}/roledetails"
category: "Project roles"
writes_data: false
tool_note: "[[jira_get_project_role_details]]"
---
# Jira v3 - Get project role details

**Get project role details** — `GET /rest/api/3/project/{projectIdOrKey}/roledetails`

- Run by the tool [[jira_get_project_role_details]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/roledetails?currentMember={{param:currentMember}}&excludeConnectAddons={{param:excludeConnectAddons}}&excludeOtherServiceRoles={{param:excludeOtherServiceRoles}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).
- `currentMember` (query, string, optional) — Whether the roles should be filtered to include only those the user is assigned to.
- `excludeConnectAddons` (query, string, optional) — Query parameter excludeConnectAddons.
- `excludeOtherServiceRoles` (query, string, optional) — Do not return the default JSM company-managed space from CSM spaces, or the default CSM roles from JSM spaces.

## Original description

Returns all [project roles](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/) and the details for each role. Note that the list of project roles is common to all projects.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
