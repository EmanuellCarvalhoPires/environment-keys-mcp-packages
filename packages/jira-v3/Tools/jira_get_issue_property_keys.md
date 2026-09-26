---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-properties
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_property_keys
title: "Jira v3 - Get issue property keys"
kind: request
request: "[[Jira v3 - Get issue property keys]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/{issueIdOrKey}/properties · Get issue property keys. Returns the URLs and keys of an issue's properties. This operation can be accessed anonymously. Permissions required: Property details are only returned where the user has: Browse projects project permission for the project containing the issue. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The key or ID of the issue."
writes: false
expose: false
---
# jira_get_issue_property_keys

`GET /rest/api/3/issue/{issueIdOrKey}/properties` — Get issue property keys

- Request: [[Jira v3 - Get issue property keys]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
