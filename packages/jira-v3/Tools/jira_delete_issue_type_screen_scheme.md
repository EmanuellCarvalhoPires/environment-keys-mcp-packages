---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-screen-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_issue_type_screen_scheme
title: "Jira v3 - Delete issue type screen scheme"
kind: request
request: "[[Jira v3 - Delete issue type screen scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId} · Delete issue type screen scheme. Deletes an issue type screen scheme. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "issueTypeScreenSchemeId":
    type: string
    required: true
    description: "The ID of the issue type screen scheme."
writes: true
expose: false
---
# jira_delete_issue_type_screen_scheme

`DELETE /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}` — Delete issue type screen scheme

- Request: [[Jira v3 - Delete issue type screen scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
