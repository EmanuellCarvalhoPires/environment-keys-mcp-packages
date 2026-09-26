---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-types
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_all_issue_types_for_user
title: "Jira v3 - Get all issue types for user"
kind: request
request: "[[Jira v3 - Get all issue types for user]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issuetype · Get all issue types for user. Returns all issue types. This operation can be accessed anonymously. Permissions required: Issue types are only returned as follows: if the user has the Administer Jira global permission, all issue types are returned. Writes data: no."
writes: false
expose: false
---
# jira_get_all_issue_types_for_user

`GET /rest/api/3/issuetype` — Get all issue types for user

- Request: [[Jira v3 - Get all issue types for user]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
