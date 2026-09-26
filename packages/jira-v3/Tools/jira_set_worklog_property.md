---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklog-properties
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_set_worklog_property
title: "Jira v3 - Set worklog property"
kind: request
request: "[[Jira v3 - Set worklog property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey} · Set worklog property. Sets the value of a worklog property. Use this operation to store custom data against the worklog. The value of the request body must be a valid, non-empty JSON blob. The maximum length is 32768 characters. This operation can be accessed anonymously. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "worklogId":
    type: string
    required: true
    description: "The ID of the worklog."
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
# jira_set_worklog_property

`PUT /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}` — Set worklog property

- Request: [[Jira v3 - Set worklog property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
