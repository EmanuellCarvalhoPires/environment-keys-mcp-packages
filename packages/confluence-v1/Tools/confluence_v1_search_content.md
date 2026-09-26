---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/search
  - api/operation/search
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_search_content
title: "Confluence v1 - Search content"
kind: request
request: "[[Confluence v1 - Search content]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/search · Search content. Searches for content using the Confluence Query Language (CQL). Note that CQL input queries submitted through the /wiki/rest/api/search endpoint no longer support user-specific fields like user, user.fullname, user.accountid, and user.userkey. Writes data: no."
params:
  "cql":
    type: string
    required: true
    description: "The CQL query to be used for the search. See Advanced Searching using CQL for instructions on how to build a CQL query."
  "cqlcontext":
    type: string
    required: false
    description: "The space, content, and content status to execute the search against. - spaceKey Key of the space to search against. Optional. - contentId ID of the content to search against. Optional."
  "cursor":
    type: string
    required: false
    description: "Pointer to a set of search results, returned as part of the next or prev URL from the previous search call."
  "next":
    type: string
    required: false
    description: "Query parameter next."
  "prev":
    type: string
    required: false
    description: "Query parameter prev."
  "limit":
    type: string
    required: false
    description: "The maximum number of content objects to return per page. Note, this may be restricted by fixed system limits."
  "start":
    type: string
    required: false
    description: "The start point of the collection to return"
  "includeArchivedSpaces":
    type: string
    required: false
    description: "Whether to include content from archived spaces in the results."
  "excludeCurrentSpaces":
    type: string
    required: false
    description: "Whether to exclude current spaces and only show archived spaces."
  "excerpt":
    type: string
    required: false
    description: "The excerpt strategy to apply to the result"
  "sitePermissionTypeFilter":
    type: string
    required: false
    description: "Filters users by permission type. Use none to default to licensed users, externalCollaborator for external/guest users, and all to include all permission types."
  "_":
    type: string
    required: false
    description: "Query parameter ."
  "expand":
    type: string
    required: false
    description: "Query parameter expand."
writes: false
expose: false
---
# confluence_v1_search_content

`GET /wiki/rest/api/search` — Search content

- Request: [[Confluence v1 - Search content]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
