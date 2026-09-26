---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_remove_member_from_issue_security_level
title: "Jira v3 - Remove member from issue security level"
kind: request
request: "[[Jira v3 - Remove member from issue security level]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member/{memberId} · Remove member from issue security level. Removes an issue security level member from an issue security scheme. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "schemeId":
    type: string
    required: true
    description: "The ID of the issue security scheme."
  "levelId":
    type: string
    required: true
    description: "The ID of the issue security level."
  "memberId":
    type: string
    required: true
    description: "The ID of the issue security level member to be removed."
writes: true
expose: false
---
# jira_remove_member_from_issue_security_level

`DELETE /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member/{memberId}` — Remove member from issue security level

- Request: [[Jira v3 - Remove member from issue security level]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
