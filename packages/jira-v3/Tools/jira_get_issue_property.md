---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-properties
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_property
title: "Jira v3 - Get issue property"
kind: request
request: "[[Jira v3 - Get issue property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey} · Get issue property. Returns the key and value of an issue's property. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project containing the issue. If issue-level security is configured, issue-level security permission to view the issue. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The key or ID of the issue."
  "propertyKey":
    type: string
    required: true
    description: "The key of the property."
writes: false
expose: false
---
# jira_get_issue_property

`GET /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}` — Get issue property

- Request: [[Jira v3 - Get issue property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
