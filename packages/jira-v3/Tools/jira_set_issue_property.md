---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-properties
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_set_issue_property
title: "Jira v3 - Set issue property"
kind: request
request: "[[Jira v3 - Set issue property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey} · Set issue property. Sets the value of an issue's property. Use this resource to store custom data against an issue. The value of the request body must be a valid, non-empty JSON blob. The maximum length is 32768 characters. This operation can be accessed anonymously. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "propertyKey":
    type: string
    required: true
    description: "The key of the issue property. The maximum length is 255 characters."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_issue_property

`PUT /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}` — Set issue property

- Request: [[Jira v3 - Set issue property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
