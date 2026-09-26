---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_create_metadata_issue_types_for_a_project
title: "Jira v3 - Get create metadata issue types for a project"
kind: request
request: "[[Jira v3 - Get create metadata issue types for a project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes · Get create metadata issue types for a project. Returns a page of issue type metadata for a specified project. Use the information to populate the requests in Create issue and Create issues. This operation can be accessed anonymously. Permissions required: Create issues project permission in the requested projects. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The ID or key of the project."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
writes: false
expose: false
---
# jira_get_create_metadata_issue_types_for_a_project

`GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes` — Get create metadata issue types for a project

- Request: [[Jira v3 - Get create metadata issue types for a project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
