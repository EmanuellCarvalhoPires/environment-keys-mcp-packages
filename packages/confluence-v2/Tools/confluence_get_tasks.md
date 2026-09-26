---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/task
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_tasks
title: "Confluence v2 - Get tasks"
kind: request
request: "[[Confluence v2 - Get tasks]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /tasks · Get tasks. Returns all tasks. The number of results is limited by the limit parameter and additional results (if available) will be available through the next URL present in the Link response header. Writes data: no."
params:
  "body_format":
    type: string
    required: false
    description: "The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field."
  "include_blank_tasks":
    type: string
    required: false
    description: "Specifies whether to include blank tasks in the response. Defaults to true."
  "status":
    type: string
    required: false
    description: "Filters on the status of the task."
  "task_id":
    type: string
    required: false
    description: "Filters on task ID. Multiple IDs can be specified."
  "space_id":
    type: string
    required: false
    description: "Filters on the space ID of the task. Multiple IDs can be specified."
  "page_id":
    type: string
    required: false
    description: "Filters on the page ID of the task. Multiple IDs can be specified. Note - page and blog post filters can be used in conjunction."
  "blogpost_id":
    type: string
    required: false
    description: "Filters on the blog post ID of the task. Multiple IDs can be specified. Note - page and blog post filters can be used in conjunction."
  "created_by":
    type: string
    required: false
    description: "Filters on the Account ID of the user who created this task. Multiple IDs can be specified."
  "assigned_to":
    type: string
    required: false
    description: "Filters on the Account ID of the user to whom this task is assigned. Multiple IDs can be specified."
  "completed_by":
    type: string
    required: false
    description: "Filters on the Account ID of the user who completed this task. Multiple IDs can be specified."
  "created_at_from":
    type: string
    required: false
    description: "Filters on start of date-time range of task based on creation date (inclusive). Input is epoch time in milliseconds."
  "created_at_to":
    type: string
    required: false
    description: "Filters on end of date-time range of task based on creation date (inclusive). Input is epoch time in milliseconds."
  "due_at_from":
    type: string
    required: false
    description: "Filters on start of date-time range of task based on due date (inclusive). Input is epoch time in milliseconds."
  "due_at_to":
    type: string
    required: false
    description: "Filters on end of date-time range of task based on due date (inclusive). Input is epoch time in milliseconds."
  "completed_at_from":
    type: string
    required: false
    description: "Filters on start of date-time range of task based on completion date (inclusive). Input is epoch time in milliseconds."
  "completed_at_to":
    type: string
    required: false
    description: "Filters on end of date-time range of task based on completion date (inclusive). Input is epoch time in milliseconds."
  "cursor":
    type: string
    required: false
    description: "Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results."
  "limit":
    type: string
    required: false
    description: "Maximum number of tasks per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results."
writes: false
expose: false
---
# confluence_get_tasks

`GET /tasks` — Get tasks

- Request: [[Confluence v2 - Get tasks]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
