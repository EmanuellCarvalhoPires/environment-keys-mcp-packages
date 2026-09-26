---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-properties
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_issue_property
title: "Jira v3 - Delete issue property"
kind: request
request: "[[Jira v3 - Delete issue property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey} · Delete issue property. Deletes an issue's property. This operation can be accessed anonymously. Permissions required: Browse projects and Edit issues project permissions for the project containing the issue. If issue-level security is configured, issue-level security permission to view the issue. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The key or ID of the issue."
  "propertyKey":
    type: string
    required: true
    description: "The key of the property."
writes: true
expose: false
---
# jira_delete_issue_property

`DELETE /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}` — Delete issue property

- Request: [[Jira v3 - Delete issue property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
