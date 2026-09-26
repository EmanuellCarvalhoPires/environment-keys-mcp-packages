---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-properties
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_project_property
title: "Jira v3 - Get project property"
kind: request
request: "[[Jira v3 - Get project property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey} · Get project property. Returns the value of a project property. This operation can be accessed anonymously. Permissions required: Browse Projects project permission for the project containing the property. Writes data: no."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
  "propertyKey":
    type: string
    required: true
    description: "The project property key. Use Get project property keys to get a list of all project property keys."
writes: false
expose: false
---
# jira_get_project_property

`GET /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}` — Get project property

- Request: [[Jira v3 - Get project property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
