---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_change_order_of_issue_types
title: "Jira v3 - Change order of issue types"
kind: request
request: "[[Jira v3 - Change order of issue types]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move · Change order of issue types. Changes the order of issue types in an issue type scheme. The request body parameters must meet the following requirements: all of the issue types must belong to the issue type scheme. either after or position must be provided. Writes data: yes."
params:
  "issueTypeSchemeId":
    type: string
    required: true
    description: "The ID of the issue type scheme."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_change_order_of_issue_types

`PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move` — Change order of issue types

- Request: [[Jira v3 - Change order of issue types]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
