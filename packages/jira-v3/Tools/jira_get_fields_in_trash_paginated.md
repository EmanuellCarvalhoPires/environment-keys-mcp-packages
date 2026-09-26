---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_fields_in_trash_paginated
title: "Jira v3 - Get fields in trash paginated"
kind: request
request: "[[Jira v3 - Get fields in trash paginated]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/field/search/trashed · Get fields in trash paginated. Returns a paginated list of fields in the trash. The list may be restricted to fields whose field name or description partially match a string. Only custom fields can be queried, type must be set to custom. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "id":
    type: string
    required: false
    description: "Query parameter id."
  "query":
    type: string
    required: false
    description: "String used to perform a case-insensitive partial match with field names or descriptions."
  "expand":
    type: string
    required: false
    description: "Query parameter expand."
  "orderBy":
    type: string
    required: false
    description: "Order the results by a field: name sorts by the field name trashDate sorts by the date the field was moved to the trash plannedDeletionDate sorts by the planned deletion date"
writes: false
expose: false
---
# jira_get_fields_in_trash_paginated

`GET /rest/api/3/field/search/trashed` — Get fields in trash paginated

- Request: [[Jira v3 - Get fields in trash paginated]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
