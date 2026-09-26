---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content
  - api/operation/search
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_search_content_by_cql
title: "Confluence v1 - Search content by CQL"
kind: request
request: "[[Confluence v1 - Search content by CQL]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/content/search · Search content by CQL. Returns the list of content that matches a Confluence Query Language (CQL) query. For information on CQL, see: Advanced searching using CQL. Example initial call: /wiki/rest/api/content/search?cql=type=page&limit=25 Example response: { \"results\": [ { ... }, { ... }, ... { ... Writes data: no."
params:
  "cql":
    type: string
    required: true
    description: "The CQL string that is used to find the requested content."
  "cqlcontext":
    type: string
    required: false
    description: "The space, content, and content status to execute the search against. Specify this as an object with the following properties: - spaceKey Key of the space to search against. Optional."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the content to expand. - childTypes.all returns whether the content has attachments, comments, or child pages/whiteboards."
  "cursor":
    type: string
    required: false
    description: "Pointer to a set of search results, returned as part of the next or prev URL from the previous search call."
  "limit":
    type: string
    required: false
    description: "The maximum number of content objects to return per page. Note, this may be restricted by fixed system limits."
writes: false
expose: true
---
# confluence_v1_search_content_by_cql

`GET /wiki/rest/api/content/search` — Search content by CQL

- Request: [[Confluence v1 - Search content by CQL]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
