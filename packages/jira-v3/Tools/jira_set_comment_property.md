---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comment-properties
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_set_comment_property
title: "Jira v3 - Set comment property"
kind: request
request: "[[Jira v3 - Set comment property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/comment/{commentId}/properties/{propertyKey} · Set comment property. Creates or updates the value of a property for a comment. Use this resource to store custom data against a comment. The value of the request body must be a valid, non-empty JSON blob. The maximum length is 32768 characters. Writes data: yes."
params:
  "commentId":
    type: string
    required: true
    description: "The ID of the comment."
  "propertyKey":
    type: string
    required: true
    description: "The key of the property. The maximum length is 255 characters."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_comment_property

`PUT /rest/api/3/comment/{commentId}/properties/{propertyKey}` — Set comment property

- Request: [[Jira v3 - Set comment property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
