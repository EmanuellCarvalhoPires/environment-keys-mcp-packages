---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_create_field_metadata_for_a_project_and_issue_type_id
title: "Jira v3 - Get create field metadata for a project and issue type id"
kind: request
request: "[[Jira v3 - Get create field metadata for a project and issue type id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId} · Get create field metadata for a project and issue type id. Returns a page of field metadata for a specified project and issuetype id. Use the information to populate the requests in Create issue and Create issues. This operation can be accessed anonymously. Permissions required: Create issues project permission in the requested projects. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The ID or key of the project."
  "issueTypeId":
    type: string
    required: true
    description: "The issuetype ID."
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
# jira_get_create_field_metadata_for_a_project_and_issue_type_id

`GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId}` — Get create field metadata for a project and issue type id

- Request: [[Jira v3 - Get create field metadata for a project and issue type id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
