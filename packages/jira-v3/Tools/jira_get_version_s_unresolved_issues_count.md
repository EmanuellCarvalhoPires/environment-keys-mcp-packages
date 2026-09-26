---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_version_s_unresolved_issues_count
title: "Jira v3 - Get version's unresolved issues count"
kind: request
request: "[[Jira v3 - Get version's unresolved issues count]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/version/{id}/unresolvedIssueCount · Get version's unresolved issues count. Returns counts of the issues and unresolved issues for the project version. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project that contains the version. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the version."
writes: false
expose: false
---
# jira_get_version_s_unresolved_issues_count

`GET /rest/api/3/version/{id}/unresolvedIssueCount` — Get version's unresolved issues count

- Request: [[Jira v3 - Get version's unresolved issues count]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
