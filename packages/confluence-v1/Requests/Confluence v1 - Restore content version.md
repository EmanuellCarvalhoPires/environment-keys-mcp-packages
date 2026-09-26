---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-versions
  - api/operation/action
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/content/{id}/version"
category: "Content versions"
writes_data: true
tool_note: "[[confluence_v1_restore_content_version]]"
---
# Confluence v1 - Restore content version

**Restore content version** — `POST /wiki/rest/api/content/{id}/version`

- Run by the tool [[confluence_v1_restore_content_version]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/content/{{param:id}}/version?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the content for which the history will be restored.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the content to expand. By default, the content object is expanded. - collaborators returns the users that collaborated on the version.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Restores a historical version to be the latest version. That is, a new version
is created with the content of the historical version.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to update the content.
