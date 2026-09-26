---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-properties
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_issue_type_property
title: "Jira v3 - Delete issue type property"
kind: request
request: "[[Jira v3 - Delete issue type property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey} · Delete issue type property. Deletes the issue type property. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "issueTypeId":
    type: string
    required: true
    description: "The ID of the issue type."
  "propertyKey":
    type: string
    required: true
    description: "The key of the property. Use Get issue type property keys to get a list of all issue type property keys."
writes: true
expose: false
---
# jira_delete_issue_type_property

`DELETE /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}` — Delete issue type property

- Request: [[Jira v3 - Delete issue type property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
