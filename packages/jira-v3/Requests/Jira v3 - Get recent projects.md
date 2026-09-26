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
path: "/rest/api/3/project/recent"
category: "Projects"
writes_data: false
tool_note: "[[jira_get_recent_projects]]"
---
# Jira v3 - Get recent projects

**Get recent projects** — `GET /rest/api/3/project/recent`

- Run by the tool [[jira_get_recent_projects]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/recent?expand={{param:expand}}&properties={{param:properties}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include: description Returns the project description.
- `properties` (query, string, optional) — EXPERIMENTAL. A list of project properties to return for the project. This parameter accepts a comma-separated list. Invalid property names are ignored.

## Original description

Returns a list of up to 20 projects recently viewed by the user that are still visible to the user.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Projects are returned only where the user has one of:

 *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
