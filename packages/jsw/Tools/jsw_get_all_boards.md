---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_all_boards
title: "JSW - Get all boards"
kind: request
request: "[[JSW - Get all boards]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board · Get all boards. Returns all boards. This only includes boards that the user has permission to view. Deprecation notice: The required OAuth 2.0 scopes will be updated on February 15, 2024. read:board-scope:jira-software, read:project:jira Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The starting index of the returned boards. Base index: 0. See the 'Pagination' section at the top of this page for more details."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of boards to return per page. See the 'Pagination' section at the top of this page for more details."
  "type":
    type: string
    required: false
    description: "Filters results to boards of the specified types. Valid values: scrum, kanban, simple."
  "name":
    type: string
    required: false
    description: "Filters results to boards that match or partially match the specified name."
  "projectKeyOrId":
    type: string
    required: false
    description: "Filters results to boards that are relevant to a project. Relevance means that the jql filter defined in board contains a reference to a project."
  "accountIdLocation":
    type: string
    required: false
    description: "Query parameter accountIdLocation."
  "projectLocation":
    type: string
    required: false
    description: "Query parameter projectLocation."
  "includePrivate":
    type: string
    required: false
    description: "Appends private boards to the end of the list. The name and type fields are excluded for security reasons."
  "negateLocationFiltering":
    type: string
    required: false
    description: "If set to true, negate filters used for querying by location. By default false."
  "orderBy":
    type: string
    required: false
    description: "Ordering of the results by a given field. If not provided, values will not be sorted. Valid values: name."
  "expand":
    type: string
    required: false
    description: "List of fields to expand for each board. Valid values: admins, permissions."
  "projectTypeLocation":
    type: string
    required: false
    description: "Filters results to boards that are relevant to a project types. Support Jira Software, Jira Service Management. Valid values: software, service\\desk. By default software."
  "filterId":
    type: string
    required: false
    description: "Filters results to boards that are relevant to a filter. Not supported for next-gen boards."
writes: false
expose: true
---
# jsw_get_all_boards

`GET /rest/agile/1.0/board` — Get all boards

- Request: [[JSW - Get all boards]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
