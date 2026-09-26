---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-macro-body
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/content/{id}/history/{version}/macro/id/{macroId}/convert/async/{to}"
category: "Content - macro body"
writes_data: false
tool_note: "[[confluence_v1_get_macro_body_by_macro_id_and_convert_representat]]"
---
# Confluence v1 - Get macro body by macro ID and convert representation Asynchronously

**Get macro body by macro ID and convert representation Asynchronously** — `GET /wiki/rest/api/content/{id}/history/{version}/macro/id/{macroId}/convert/async/{to}`

- Run by the tool [[confluence_v1_get_macro_body_by_macro_id_and_convert_representat]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/content/{{param:id}}/history/{{param:version}}/macro/id/{{param:macroId}}/convert/async/{{param:to}}?expand={{param:expand}}&allowCache={{param:allowCache}}&spaceKeyContext={{param:spaceKeyContext}}&embeddedContentRender={{param:embeddedContentRender}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID for the content that contains the macro.
- `version` (path, string, required) — The version of the content that contains the macro. Specifying 0 as the version will return the macro body for the latest content version.
- `macroId` (path, string, required) — The ID of the macro. For apps, this is passed to the macro by the Connect/Forge framework.
- `to` (path, string, required) — The content representation to return the macro in. Currently, the following conversions are allowed: - exportview - styledview - view
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the content to expand and populate. Expands are dependent on the to conversion format and may be irrelevant for certain conversions (e.g.
- `allowCache` (query, string, optional) — Controls whether conversion results are cached and reused for identical requests. - false: Each request creates a new conversion task, even if an identical request was made previously.
- `spaceKeyContext` (query, string, optional) — The space key used for resolving embedded content (page includes, files, and links) in the content body.
- `embeddedContentRender` (query, string, optional) — Mode used for rendering embedded content, like attachments. - current renders the embedded content using the latest version.

## Original description

Returns Async Id of the conversion task which will convert the macro into a content body of the desired format.
The result will be available for 5 minutes after completion of the conversion.

About the macro ID: When a macro is created in a new version of content,
Confluence will generate a random ID for it, unless an ID is specified
(by an app). The macro ID will look similar to this: '884bd9-0cb8-41d5-98be-f80943c14f96'.
The ID is then persisted as new versions of content are created, and is
only modified by Confluence if there are conflicting IDs.

For Forge macros, the value for macro ID is the "local ID" of that particular ADF node.
This value can be retrieved either client-side by calling view.getContext() and accessing "localId"
on the resulting object, or server-side by examining the "local-id" parameter node inside the "parameters" node.

Note that there are other attributes named "local-id", but only this particular one is used to store the macro ID.

Example:

  com.atlassian.ecosystem
  
      e9c4aa10-73fa-417c-888d-48c719ae4165
  


Note, to preserve backwards compatibility this resource will also match on
the hash of the macro body, even if a macro ID is found. This check will
eventually become redundant, as macro IDs are generated for pages and
transparently propagate out to all instances.

This backwards compatibility logic does not apply to Forge macros; those
can only be retrieved by their ID.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the content that the macro is in.
