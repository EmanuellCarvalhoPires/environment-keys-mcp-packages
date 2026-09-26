---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/version/{id}/relatedwork"
category: "Project versions"
writes_data: true
tool_note: "[[jira_update_related_work]]"
---
# Jira v3 - Update related work

**Update related work** — `PUT /rest/api/3/version/{id}/relatedwork`

- Run by the tool [[jira_update_related_work]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/version/{{param:id}}/relatedwork
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the version to update the related work on. For the related work id, pass it to the input JSON.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "category": "Design",
  "relatedWorkId": "fabcdef6-7878-1234-beaf-43211234abcd",
  "title": "Design link",
  "url": "https://www.atlassian.com"
}
```

## Original description

Updates the given related work. You can only update generic link related works via Rest APIs. Any archived version related works can't be edited.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Resolve issues:* and *Edit issues* [Managing project permissions](https://confluence.atlassian.com/adminjiraserver/managing-project-permissions-938847145.html) for the project that contains the version.
