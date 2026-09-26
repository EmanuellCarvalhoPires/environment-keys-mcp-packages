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
tool: confluence_v1_get_content_in_space_with_given_content_state
title: "Confluence v1 - Get content in space with given content state"
kind: request
request: "[[Confluence v1 - Get content in space with given content state]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/space/{spaceKey}/state/content · Get content in space with given content state. Returns all content that has the provided content state in a space. If the expand query parameter is used with the body.exportview and/or body.styledview properties, then the query limit parameter will be restricted to a maximum value of 25. Writes data: no."
params:
  "spaceKey":
    type: string
    required: true
    description: "The key of the space to be queried for its content state settings."
  "state_id":
    type: string
    required: true
    description: "The id of the content state to filter content by"
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the content to expand. Options include: space, version, history, children, etc. Ex: space,version"
  "limit":
    type: string
    required: false
    description: "Maximum number of results to return"
  "start":
    type: string
    required: false
    description: "Number of result to start returning. (0 indexed)"
writes: false
expose: false
---
# confluence_v1_get_content_in_space_with_given_content_state

`GET /wiki/rest/api/space/{spaceKey}/state/content` — Get content in space with given content state

- Request: [[Confluence v1 - Get content in space with given content state]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
