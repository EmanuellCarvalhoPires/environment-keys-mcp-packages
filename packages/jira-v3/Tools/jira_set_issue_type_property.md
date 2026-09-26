---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-properties
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_set_issue_type_property
title: "Jira v3 - Set issue type property"
kind: request
request: "[[Jira v3 - Set issue type property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey} · Set issue type property. Creates or updates the value of the issue type property. Use this resource to store and update data against an issue type. The value of the request body must be a valid, non-empty JSON blob. The maximum length is 32768 characters. Writes data: yes."
params:
  "issueTypeId":
    type: string
    required: true
    description: "The ID of the issue type."
  "propertyKey":
    type: string
    required: true
    description: "The key of the issue type property. The maximum length is 255 characters."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_issue_type_property

`PUT /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}` — Set issue type property

- Request: [[Jira v3 - Set issue type property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
