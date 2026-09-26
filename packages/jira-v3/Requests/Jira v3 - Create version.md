---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/version"
category: "Project versions"
writes_data: true
tool_note: "[[jira_create_version]]"
---
# Jira v3 - Create version

**Create version** — `POST /rest/api/3/version`

- Run by the tool [[jira_create_version]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/version
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "archived": false,
  "description": "An excellent version",
  "name": "New Version 1",
  "projectId": 10000,
  "releaseDate": "2010-07-06",
  "released": true
}
```

## Original description

Creates a project version.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the version is added to.
