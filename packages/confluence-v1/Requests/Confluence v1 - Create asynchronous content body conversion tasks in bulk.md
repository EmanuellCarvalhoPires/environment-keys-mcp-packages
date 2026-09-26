---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-body
  - api/operation/create
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/contentbody/convert/async/bulk/tasks"
category: "Content body"
writes_data: true
tool_note: "[[confluence_v1_create_asynchronous_content_body_conversion_tasks]]"
---
# Confluence v1 - Create asynchronous content body conversion tasks in bulk

**Create asynchronous content body conversion tasks in bulk** — `POST /wiki/rest/api/contentbody/convert/async/bulk/tasks`

- Run by the tool [[confluence_v1_create_asynchronous_content_body_conversion_tasks]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/contentbody/convert/async/bulk/tasks
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Asynchronously converts content bodies from one format to another format in bulk. Use the Content body
REST API to get the status of conversion tasks. Note that there is a maximum limit of 10 conversions per
request to this endpoint.

Supported conversions:

- storage: editor, export_view, styled_view, view
- editor: storage

Once a conversion task is completed, it is available for polling for up to 5 minutes.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
'View' permission for the space, and permission to view the content if the `spaceKeyContext` or
`contentIdContext` are present.
