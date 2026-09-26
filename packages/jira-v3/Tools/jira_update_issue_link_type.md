---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-link-types
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_issue_link_type
title: "Jira v3 - Update issue link type"
kind: request
request: "[[Jira v3 - Update issue link type]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issueLinkType/{issueLinkTypeId} · Update issue link type. Updates an issue link type. To use this operation, the site must have issue linking enabled. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "issueLinkTypeId":
    type: string
    required: true
    description: "The ID of the issue link type."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_issue_link_type

`PUT /rest/api/3/issueLinkType/{issueLinkTypeId}` — Update issue link type

- Request: [[Jira v3 - Update issue link type]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
