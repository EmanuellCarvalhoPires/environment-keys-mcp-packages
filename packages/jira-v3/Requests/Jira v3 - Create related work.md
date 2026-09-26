---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/version/{id}/relatedwork"
category: "Project versions"
writes_data: true
tool_note: "[[jira_create_related_work]]"
---
# Jira v3 - Create related work

**Create related work** — `POST /rest/api/3/version/{id}/relatedwork`

- Run by the tool [[jira_create_related_work]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/version/{{param:id}}/relatedwork
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "category": "Design",
  "title": "Design link",
  "url": "https://www.atlassian.com"
}
```

## Original description

Creates a related work for the given version. You can only create a generic link type of related works via this API. relatedWorkId will be auto-generated UUID, that does not need to be provided.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Resolve issues:* and *Edit issues* [Managing project permissions](https://confluence.atlassian.com/adminjiraserver/managing-project-permissions-938847145.html) for the project that contains the version.
