---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-states
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_gets_available_content_states_for_content
title: "Confluence v1 - Gets available content states for content"
kind: request
request: "[[Confluence v1 - Gets available content states for content]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/{id}/state/available · Gets available content states for content.. Gets content states that are available for the content to be set as. Will return all enabled Space Content States. Will only return most the 3 most recently published custom content states to match UI editor list. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "id of content to get available states for"
writes: false
expose: false
---
# confluence_v1_gets_available_content_states_for_content

`GET /wiki/rest/api/content/{id}/state/available` — Gets available content states for content.

- Request: [[Confluence v1 - Gets available content states for content]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
