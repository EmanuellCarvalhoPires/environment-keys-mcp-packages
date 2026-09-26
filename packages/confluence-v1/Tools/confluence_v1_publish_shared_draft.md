---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_publish_shared_draft
title: "Confluence v1 - Publish shared draft"
kind: request
request: "[[Confluence v1 - Publish shared draft]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · PUT /wiki/rest/api/content/blueprint/instance/{draftId} · Publish shared draft. Publishes a shared draft of a page created from a blueprint. By default, the following objects are expanded: body.storage, history, space, version, ancestors. Writes data: yes."
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
# confluence_v1_publish_shared_draft

`PUT /wiki/rest/api/content/blueprint/instance/{draftId}` — Publish shared draft

- Request: [[Confluence v1 - Publish shared draft]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
