---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_move_version
title: "Jira v3 - Move version"
kind: request
request: "[[Jira v3 - Move version]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/version/{id}/move · Move version. Modifies the version's sequence within the project, which affects the display order of the versions in Jira. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project that contains the version. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the version to be moved."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_move_version

`POST /rest/api/3/version/{id}/move` — Move version

- Request: [[Jira v3 - Move version]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
