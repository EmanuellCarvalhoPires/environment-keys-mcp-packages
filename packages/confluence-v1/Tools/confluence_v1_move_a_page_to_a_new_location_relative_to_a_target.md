---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-children-and-descendants
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_move_a_page_to_a_new_location_relative_to_a_target
title: "Confluence v1 - Move a page to a new location relative to a target page"
kind: request
request: "[[Confluence v1 - Move a page to a new location relative to a target page]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · PUT /wiki/rest/api/content/{pageId}/move/{position}/{targetId} · Move a page to a new location relative to a target page. Move a page to a new location relative to a target page: before - move the page under the same parent as the target, before the target in the list of children after - move the page under the same parent as the target, after the target in the list of children append - move the pag… Writes data: yes."
params:
  "pageId":
    type: string
    required: true
    description: "The ID of the page to be moved"
  "position":
    type: string
    required: true
    description: "The position to move the page to relative to the target page: before - move the page under the same parent as the target, before the target in the list of children after - move the page under the same…"
  "targetId":
    type: string
    required: true
    description: "The ID of the target page for this operation"
writes: true
expose: false
---
# confluence_v1_move_a_page_to_a_new_location_relative_to_a_target

`PUT /wiki/rest/api/content/{pageId}/move/{position}/{targetId}` — Move a page to a new location relative to a target page

- Request: [[Confluence v1 - Move a page to a new location relative to a target page]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
