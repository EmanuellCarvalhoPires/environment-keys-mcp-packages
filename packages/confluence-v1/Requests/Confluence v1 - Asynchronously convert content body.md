---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-body
  - api/operation/action
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/contentbody/convert/async/{to}"
category: "Content body"
writes_data: true
tool_note: "[[confluence_v1_asynchronously_convert_content_body]]"
---
# Confluence v1 - Asynchronously convert content body

**Asynchronously convert content body** — `POST /wiki/rest/api/contentbody/convert/async/{to}`

- Run by the tool [[confluence_v1_asynchronously_convert_content_body]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/contentbody/convert/async/{{param:to}}?expand={{param:expand}}&spaceKeyContext={{param:spaceKeyContext}}&contentIdContext={{param:contentIdContext}}&allowCache={{param:allowCache}}&embeddedContentRender={{param:embeddedContentRender}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `to` (path, string, required) — The name of the target format for the content body.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the content to expand and populate. Expands are dependent on the to conversion format and may be irrelevant for certain conversions (e.g.
- `spaceKeyContext` (query, string, optional) — The space key used for resolving embedded content (page includes, files, and links) in the content body.
- `contentIdContext` (query, string, optional) — The content ID used to find the space for resolving embedded content (page includes, files, and links) in the content body.
- `allowCache` (query, string, optional) — Controls whether conversion results are cached and reused for identical requests. - false: Each request creates a new conversion task, even if an identical request was made previously.
- `embeddedContentRender` (query, string, optional) — Mode used for rendering embedded content, like attachments. - current renders the embedded content using the latest version.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Converts a content body from one format to another format asynchronously.
Returns the asyncId for the asynchronous task.

Supported conversions:

- atlas_doc_format: editor, export_view, storage, styled_view, view
- storage: atlas_doc_format, editor, export_view, styled_view, view
- editor: storage

No other conversions are supported at the moment.
Once a conversion is completed, it will be available for 5 minutes at the result endpoint.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
If request specifies 'contentIdContext', 'View' permission for the space, and permission to view the content.
