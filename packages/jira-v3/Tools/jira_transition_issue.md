---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_transition_issue
title: "Jira v3 - Transition issue"
kind: request
request: "[[Jira v3 - Transition issue]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issue/{issueIdOrKey}/transitions · Transition issue. Performs an issue transition and, if the transition has a screen, updates the fields from the transition screen. sortByCategory To update the fields on the transition screen, specify the fields in the fields or update parameters in the request body. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: true
---
# jira_transition_issue

`POST /rest/api/3/issue/{issueIdOrKey}/transitions` — Transition issue

- Request: [[Jira v3 - Transition issue]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
