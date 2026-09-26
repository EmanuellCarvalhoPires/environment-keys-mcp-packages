---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content
  - api/operation/action
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_publish_legacy_draft
title: "Confluence v1 - Publish legacy draft"
kind: request
request: "[[Confluence v1 - Publish legacy draft]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/content/blueprint/instance/{draftId} · Publish legacy draft. Publishes a legacy draft of a page created from a blueprint. Legacy drafts will eventually be removed in favor of shared drafts. For now, this method works the same as Publish shared draft. Writes data: yes."
params:
  "draftId":
    type: string
    required: true
    description: "The ID of the draft page that was created from a blueprint. You can find the draftId in the Confluence application by opening the draft page and checking the page URL."
  "status":
    type: string
    required: false
    description: "The status of the content to be updated, i.e. the draft. This is set to 'draft' by default, so you shouldn't need to specify it."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the content to expand. - childTypes.all returns whether the content has attachments, comments, or child pages/whiteboards."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_publish_legacy_draft

`POST /wiki/rest/api/content/blueprint/instance/{draftId}` — Publish legacy draft

- Request: [[Confluence v1 - Publish legacy draft]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
