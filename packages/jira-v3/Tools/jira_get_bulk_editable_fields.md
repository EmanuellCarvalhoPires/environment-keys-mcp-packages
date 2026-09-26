---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-bulk-operations
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_bulk_editable_fields
title: "Jira v3 - Get bulk editable fields"
kind: request
request: "[[Jira v3 - Get bulk editable fields]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/bulk/issues/fields · Get bulk editable fields. Use this API to get a list of fields visible to the user to perform bulk edit operations. You can pass single or multiple issues in the query to get eligible editable fields. This API uses pagination to return responses, delivering 50 fields at a time. Writes data: no."
params:
  "issueIdsOrKeys":
    type: string
    required: true
    description: "The IDs or keys of the issues to get editable fields from."
  "searchText":
    type: string
    required: false
    description: "(Optional)The text to search for in the editable fields."
  "endingBefore":
    type: string
    required: false
    description: "(Optional)The end cursor for use in pagination."
  "startingAfter":
    type: string
    required: false
    description: "(Optional)The start cursor for use in pagination."
writes: false
expose: false
---
# jira_get_bulk_editable_fields

`GET /rest/api/3/bulk/issues/fields` — Get bulk editable fields

- Request: [[Jira v3 - Get bulk editable fields]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
