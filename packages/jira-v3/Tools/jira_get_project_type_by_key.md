---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-types
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_project_type_by_key
title: "Jira v3 - Get project type by key"
kind: request
request: "[[Jira v3 - Get project type by key]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/type/{projectTypeKey} · Get project type by key. Returns a project type. This operation can be accessed anonymously. Permissions required: None. Writes data: no."
params:
  "projectTypeKey":
    type: string
    required: true
    description: "The key of the project type."
writes: false
expose: false
---
# jira_get_project_type_by_key

`GET /rest/api/3/project/type/{projectTypeKey}` — Get project type by key

- Request: [[Jira v3 - Get project type by key]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
