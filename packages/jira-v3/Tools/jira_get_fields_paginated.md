---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_fields_paginated
title: "Jira v3 - Get fields paginated"
kind: request
request: "[[Jira v3 - Get fields paginated]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/field/search · Get fields paginated. Returns a paginated list of fields for Classic Jira projects. The list can include: all fields specific fields, by defining id fields that contain a string in the field name or description, by defining query specific fields that contain a string in the field name or description,… Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "type":
    type: string
    required: false
    description: "The type of fields to search."
  "id":
    type: string
    required: false
    description: "The IDs of the custom fields to return or, where query is specified, filter."
  "query":
    type: string
    required: false
    description: "String used to perform a case-insensitive partial match with field names or descriptions."
  "orderBy":
    type: string
    required: false
    description: "Order the results by: contextsCount sorts by the number of contexts related to a field lastUsed sorts by the date when the value of the field last changed name sorts by the field name screensCount sor…"
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list."
  "projectIds":
    type: string
    required: false
    description: "The IDs of the projects to filter the fields by. Fields belonging to project Ids that the user does not have access to will not be returned"
writes: false
expose: false
---
# jira_get_fields_paginated

`GET /rest/api/3/field/search` — Get fields paginated

- Request: [[Jira v3 - Get fields paginated]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
