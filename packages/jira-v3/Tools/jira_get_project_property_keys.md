---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-properties
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_project_property_keys
title: "Jira v3 - Get project property keys"
kind: request
request: "[[Jira v3 - Get project property keys]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectIdOrKey}/properties · Get project property keys. Returns all project property keys for the project. This operation can be accessed anonymously. Permissions required: Browse Projects project permission for the project. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
writes: false
expose: false
---
# jira_get_project_property_keys

`GET /rest/api/3/project/{projectIdOrKey}/properties` — Get project property keys

- Request: [[Jira v3 - Get project property keys]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
