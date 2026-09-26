---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklog-properties
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_worklog_property_keys
title: "Jira v3 - Get worklog property keys"
kind: request
request: "[[Jira v3 - Get worklog property keys]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties · Get worklog property keys. Returns the keys of all properties for a worklog. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project that the issue is in. If issue-level security is configured, issue-level security permission to view the issue. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "worklogId":
    type: string
    required: true
    description: "The ID of the worklog."
writes: false
expose: false
---
# jira_get_worklog_property_keys

`GET /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties` — Get worklog property keys

- Request: [[Jira v3 - Get worklog property keys]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
