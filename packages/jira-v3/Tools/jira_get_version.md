---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_version
title: "Jira v3 - Get version"
kind: request
request: "[[Jira v3 - Get version]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/version/{id} · Get version. Returns a project version. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project containing the version. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the version."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about version in the response. This parameter accepts a comma-separated list."
writes: false
expose: false
---
# jira_get_version

`GET /rest/api/3/version/{id}` — Get version

- Request: [[Jira v3 - Get version]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
