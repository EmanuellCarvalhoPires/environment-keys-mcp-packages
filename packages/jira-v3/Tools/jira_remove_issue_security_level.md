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
tool: jira_remove_issue_security_level
title: "Jira v3 - Remove issue security level"
kind: request
request: "[[Jira v3 - Remove issue security level]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId} · Remove issue security level. Deletes an issue security level. This operation is asynchronous. Follow the location link in the response to determine the status of the task and use Get task to obtain subsequent updates. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "schemeId":
    type: string
    required: true
    description: "The ID of the issue security scheme."
  "levelId":
    type: string
    required: true
    description: "The ID of the issue security level to remove."
  "replaceWith":
    type: string
    required: false
    description: "The ID of the issue security level that will replace the currently selected level."
writes: true
expose: false
---
# jira_remove_issue_security_level

`DELETE /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}` — Remove issue security level

- Request: [[Jira v3 - Remove issue security level]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
