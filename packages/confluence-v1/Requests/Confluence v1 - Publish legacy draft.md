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
path: "/wiki/rest/api/content/blueprint/instance/{draftId}"
category: "Content"
writes_data: true
tool_note: "[[confluence_v1_publish_legacy_draft]]"
---
# Confluence v1 - Publish legacy draft

**Publish legacy draft** — `POST /wiki/rest/api/content/blueprint/instance/{draftId}`

- Run by the tool [[confluence_v1_publish_legacy_draft]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/content/blueprint/instance/{{param:draftId}}?status={{param:status}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `draftId` (path, string, required) — The ID of the draft page that was created from a blueprint. You can find the draftId in the Confluence application by opening the draft page and checking the page URL.
- `status` (query, string, optional) — The status of the content to be updated, i.e. the draft. This is set to 'draft' by default, so you shouldn't need to specify it.
- `expand` (query, string, optional) — A multi-value parameter indicating which properties of the content to expand. - childTypes.all returns whether the content has attachments, comments, or child pages/whiteboards.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Publishes a legacy draft of a page created from a blueprint. Legacy drafts
will eventually be removed in favor of shared drafts. For now, this method
works the same as [Publish shared draft](#api-content-blueprint-instance-draftId-put).

By default, the following objects are expanded: `body.storage`, `history`, `space`, `version`, `ancestors`.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the draft and 'Add' permission for the space that
the content will be created in.
