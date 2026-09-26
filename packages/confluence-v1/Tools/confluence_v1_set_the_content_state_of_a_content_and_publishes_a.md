---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-states
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_set_the_content_state_of_a_content_and_publishes_a
title: "Confluence v1 - Set the content state of a content and publishes a new version of the content"
kind: request
request: "[[Confluence v1 - Set the content state of a content and publishes a new version of the content]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · PUT /wiki/rest/api/content/{id}/state · Set the content state of a content and publishes a new version of the content.. Sets the content state of the content specified and creates a new version (publishes the content without changing the body) of the content with the new state. You may pass in either an id of a state, or the name and color of a desired new state. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The Id of the content whose content state is to be set."
  "status":
    type: string
    required: true
    description: "Status of content onto which state will be placed. If draft, then draft state will change. If current, state will be placed onto a new version of the content with same body as previous version."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_set_the_content_state_of_a_content_and_publishes_a

`PUT /wiki/rest/api/content/{id}/state` — Set the content state of a content and publishes a new version of the content.

- Request: [[Confluence v1 - Set the content state of a content and publishes a new version of the content]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
