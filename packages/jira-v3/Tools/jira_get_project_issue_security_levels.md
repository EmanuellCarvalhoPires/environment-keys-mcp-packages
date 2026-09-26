---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-permission-schemes
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_project_issue_security_levels
title: "Jira v3 - Get project issue security levels"
kind: request
request: "[[Jira v3 - Get project issue security levels]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectKeyOrId}/securitylevel · Get project issue security levels. Returns all issue security levels for the project that the user has access to. This operation can be accessed anonymously. Writes data: no."
params:
  "projectKeyOrId":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
writes: false
expose: false
---
# jira_get_project_issue_security_levels

`GET /rest/api/3/project/{projectKeyOrId}/securitylevel` — Get project issue security levels

- Request: [[Jira v3 - Get project issue security levels]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
