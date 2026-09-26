---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content
  - api/operation/action
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/content/archive"
category: "Content"
writes_data: true
tool_note: "[[confluence_v1_archive_pages]]"
---
# Confluence v1 - Archive pages

**Archive pages** — `POST /wiki/rest/api/content/archive`

- Run by the tool [[confluence_v1_archive_pages]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/content/archive
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Archives a list of pages. The pages to be archived are specified as a list of content IDs.
This API accepts the archival request and returns a task ID.
The archival process happens asynchronously.
Use the /longtask/ REST API to get the copy task status.

Each content ID needs to resolve to page objects that are not already in an archived state.
The content IDs need not belong to the same space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'Archive' permission for each of the pages in the corresponding space it belongs to.
