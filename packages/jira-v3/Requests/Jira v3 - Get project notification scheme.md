---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectKeyOrId}/notificationscheme"
category: "Projects"
writes_data: false
tool_note: "[[jira_get_project_notification_scheme]]"
---
# Jira v3 - Get project notification scheme

**Get project notification scheme** — `GET /rest/api/3/project/{projectKeyOrId}/notificationscheme`

- Run by the tool [[jira_get_project_notification_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectKeyOrId}}/notificationscheme?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectKeyOrId` (path, string, required) — The project ID or project key (case sensitive).
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list.

## Original description

Gets a [notification scheme](https://confluence.atlassian.com/x/8YdKLg) associated with the project.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg).
