---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-permission-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_project_issue_security_scheme
title: "Jira v3 - Get project issue security scheme"
kind: request
request: "[[Jira v3 - Get project issue security scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme · Get project issue security scheme. Returns the issue security scheme associated with the project. Permissions required: Administer Jira global permission or the Administer Projects project permission. Writes data: no."
params:
  "projectKeyOrId":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
writes: false
expose: false
---
# jira_get_project_issue_security_scheme

`GET /rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme` — Get project issue security scheme

- Request: [[Jira v3 - Get project issue security scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
