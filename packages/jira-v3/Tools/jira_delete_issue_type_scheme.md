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
tool: jira_delete_issue_type_scheme
title: "Jira v3 - Delete issue type scheme"
kind: request
request: "[[Jira v3 - Delete issue type scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId} · Delete issue type scheme. Deletes an issue type scheme. Only issue type schemes used in classic projects can be deleted. Only issue type schemes not associated with a project can be deleted A validation error will be returned if the specified scheme is associated with one or more projects. Writes data: yes."
params:
  "issueTypeSchemeId":
    type: string
    required: true
    description: "The ID of the issue type scheme."
writes: true
expose: false
---
# jira_delete_issue_type_scheme

`DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId}` — Delete issue type scheme

- Request: [[Jira v3 - Delete issue type scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
