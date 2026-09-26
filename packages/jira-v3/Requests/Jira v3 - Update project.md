---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/project/{projectIdOrKey}"
category: "Projects"
writes_data: true
tool_note: "[[jira_update_project]]"
---
# Jira v3 - Update project

**Update project** — `PUT /rest/api/3/project/{projectIdOrKey}`

- Run by the tool [[jira_update_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "assigneeType": "PROJECT_LEAD",
  "avatarId": 10200,
  "categoryId": 10120,
  "description": "Cloud migration initiative",
  "issueSecurityScheme": 10001,
  "key": "EX",
  "leadAccountId": "5b10a0effa615349cb016cd8",
  "name": "Example",
  "notificationScheme": 10021,
  "permissionScheme": 10011,
  "url": "http://atlassian.com"
}
```

## Original description

Updates the [project details](https://confluence.atlassian.com/x/ahLpNw) of a project.

All parameters are optional in the body of the request. Schemes will only be updated if they are included in the request, any omitted schemes will be left unchanged.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). is only needed when changing the schemes or project key. Otherwise you will only need *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg)
