---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_assign_issue
title: "Jira v3 - Assign issue"
kind: request
request: "[[Jira v3 - Assign issue]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issue/{issueIdOrKey}/assignee · Assign issue. Assigns an issue to a user. Use this operation when the calling user does not have the Edit Issues permission but has the Assign issue permission for the project that the issue is in. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue to be assigned."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: true
---
# jira_assign_issue

`PUT /rest/api/3/issue/{issueIdOrKey}/assignee` — Assign issue

- Request: [[Jira v3 - Assign issue]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
