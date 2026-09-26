---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
tool: jsw_get_projects
title: "JSW - Get projects"
kind: request
request: "[[JSW - Get projects]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · GET /rest/agile/1.0/board/{boardId}/project · Get projects. Returns all projects that are associated with the board, for the given board ID. If the user does not have permission to view the board, no projects will be returned at all. Returned projects are ordered by the name. Writes data: no."
params:
  "boardId":
    type: string
    required: true
    description: "The ID of the board that contains returned projects."
  "startAt":
    type: string
    required: false
    description: "The starting index of the returned projects. Base index: 0. See the 'Pagination' section at the top of this page for more details."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of projects to return per page. See the 'Pagination' section at the top of this page for more details."
writes: false
expose: false
---
# jsw_get_projects

`GET /rest/agile/1.0/board/{boardId}/project` — Get projects

- Request: [[JSW - Get projects]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
