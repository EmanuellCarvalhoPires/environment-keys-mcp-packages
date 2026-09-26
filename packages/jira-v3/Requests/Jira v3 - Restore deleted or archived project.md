---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/project/{projectIdOrKey}/restore"
category: "Projects"
writes_data: true
tool_note: "[[jira_restore_deleted_or_archived_project]]"
---
# Jira v3 - Restore deleted or archived project

**Restore deleted or archived project** — `POST /rest/api/3/project/{projectIdOrKey}/restore`

- Run by the tool [[jira_restore_deleted_or_archived_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/restore
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).

## Original description

Restores a project that has been archived or placed in the Jira recycle bin.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg)for Company managed projects.
 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project for Team managed projects.
