---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/permissions
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_permitted_projects
title: "Jira v3 - Get permitted projects"
kind: request
request: "[[Jira v3 - Get permitted projects]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/permissions/project · Get permitted projects. Returns all the projects where the user is granted a list of project permissions. This operation can be accessed anonymously. Permissions required: None. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_get_permitted_projects

`POST /rest/api/3/permissions/project` — Get permitted projects

- Request: [[Jira v3 - Get permitted projects]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
