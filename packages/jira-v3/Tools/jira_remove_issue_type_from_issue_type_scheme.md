---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_remove_issue_type_from_issue_type_scheme
title: "Jira v3 - Remove issue type from issue type scheme"
kind: request
request: "[[Jira v3 - Remove issue type from issue type scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId} · Remove issue type from issue type scheme. Removes an issue type from an issue type scheme. This operation cannot remove: any issue type used by issues. any issue types from the default issue type scheme. the last standard issue type from an issue type scheme. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "issueTypeSchemeId":
    type: string
    required: true
    description: "The ID of the issue type scheme."
  "issueTypeId":
    type: string
    required: true
    description: "The ID of the issue type."
writes: true
expose: false
---
# jira_remove_issue_type_from_issue_type_scheme

`DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId}` — Remove issue type from issue type scheme

- Request: [[Jira v3 - Remove issue type from issue type scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
