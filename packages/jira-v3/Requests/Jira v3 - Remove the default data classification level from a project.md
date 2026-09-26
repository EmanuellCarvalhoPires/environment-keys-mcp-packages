---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-classification-levels
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/project/{projectIdOrKey}/classification-level/default"
category: "Project classification levels"
writes_data: true
tool_note: "[[jira_remove_the_default_data_classification_level_from_a_project]]"
---
# Jira v3 - Remove the default data classification level from a project

**Remove the default data classification level from a project** — `DELETE /rest/api/3/project/{projectIdOrKey}/classification-level/default`

- Run by the tool [[jira_remove_the_default_data_classification_level_from_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/classification-level/default
Authorization: {{service.auth_token}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case-sensitive).

## Original description

Remove the default data classification level for a project.

**[Permissions](#permissions) required:**

 *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  *Administer jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
