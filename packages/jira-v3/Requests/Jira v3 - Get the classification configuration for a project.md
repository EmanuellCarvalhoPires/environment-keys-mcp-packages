---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-classification-levels
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectIdOrKey}/classification-config"
category: "Project classification levels"
writes_data: false
tool_note: "[[jira_get_the_classification_configuration_for_a_project]]"
---
# Jira v3 - Get the classification configuration for a project

**Get the classification configuration for a project** — `GET /rest/api/3/project/{projectIdOrKey}/classification-config`

- Run by the tool [[jira_get_the_classification_configuration_for_a_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/classification-config
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case-sensitive).

## Original description

Returns the consolidated classification configuration for a project's admin settings page.

This includes permitted classification levels (with status), the project's default classification level, the organization's default classification level, and the container override setting.

**[Permissions](#permissions) required:**

 *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  *Administer jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
