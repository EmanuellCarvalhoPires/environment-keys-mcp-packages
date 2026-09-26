---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/project/{projectIdOrKey}/archive"
category: "Projects"
writes_data: true
tool_note: "[[jira_archive_project]]"
---
# Jira v3 - Archive project

**Archive project** — `POST /rest/api/3/project/{projectIdOrKey}/archive`

- Run by the tool [[jira_archive_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/archive
Authorization: {{service.auth_token}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).

## Original description

Archives a project. You can't delete a project if it's archived. To delete an archived project, restore the project and then delete it. To restore a project, use the Jira UI.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
