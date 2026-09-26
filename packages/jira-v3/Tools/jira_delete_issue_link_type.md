---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-link-types
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_issue_link_type
title: "Jira v3 - Delete issue link type"
kind: request
request: "[[Jira v3 - Delete issue link type]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issueLinkType/{issueLinkTypeId} · Delete issue link type. Deletes an issue link type. To use this operation, the site must have issue linking enabled. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "issueLinkTypeId":
    type: string
    required: true
    description: "The ID of the issue link type."
writes: true
expose: false
---
# jira_delete_issue_link_type

`DELETE /rest/api/3/issueLinkType/{issueLinkTypeId}` — Delete issue link type

- Request: [[Jira v3 - Delete issue link type]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
