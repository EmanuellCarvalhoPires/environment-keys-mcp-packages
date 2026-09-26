---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-fields
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_field_project_associations
title: "Jira v3 - Get field project associations"
kind: request
request: "[[Jira v3 - Get field project associations]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/field/{fieldId}/association/project · Get field project associations. Returns a paginated list of project associations for the given custom field. Each association contains the ID of a project the field is associated with. Permissions required: Administer Jira global permission. Writes data: no."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the field, for example customfield10000."
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
# jira_get_field_project_associations

`GET /rest/api/3/field/{fieldId}/association/project` — Get field project associations

- Request: [[Jira v3 - Get field project associations]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
