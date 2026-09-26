---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-states
  - api/operation/delete
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_removes_the_content_state_of_a_content_and_publish
title: "Confluence v1 - Removes the content state of a content and publishes a new version"
kind: request
request: "[[Confluence v1 - Removes the content state of a content and publishes a new version]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · DELETE /wiki/rest/api/content/{id}/state · Removes the content state of a content and publishes a new version.. Removes the content state of the content specified and creates a new version (publishes the content without changing the body) of the content with the new status. Permissions required: Permission to edit the content. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The Id of the content whose content state is to be set."
  "status":
    type: string
    required: false
    description: "status of content state from which to delete state. Can be draft or archived"
writes: true
expose: false
---
# confluence_v1_removes_the_content_state_of_a_content_and_publish

`DELETE /wiki/rest/api/content/{id}/state` — Removes the content state of a content and publishes a new version.

- Request: [[Confluence v1 - Removes the content state of a content and publishes a new version]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
