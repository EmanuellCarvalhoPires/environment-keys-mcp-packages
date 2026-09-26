---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/version/{id}"
category: "Project versions"
writes_data: true
tool_note: "[[jira_update_version]]"
---
# Jira v3 - Update version

**Update version** — `PUT /rest/api/3/version/{id}`

- Run by the tool [[jira_update_version]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/version/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the version.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "archived": false,
  "description": "An excellent version",
  "id": "10000",
  "name": "New Version 1",
  "overdue": true,
  "projectId": 10000,
  "releaseDate": "2010-07-06",
  "released": true,
  "self": "https://your-domain.atlassian.net/rest/api/~ver~/version/10000",
  "userReleaseDate": "6/Jul/2010"
}
```

## Original description

Updates a project version.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.
