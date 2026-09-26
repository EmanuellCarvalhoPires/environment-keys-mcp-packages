---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_related_work
title: "Jira v3 - Get related work"
kind: request
request: "[[Jira v3 - Get related work]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/version/{id}/relatedwork · Get related work. Returns related work items for the given version id. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project containing the version. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the version."
writes: false
expose: false
---
# jira_get_related_work

`GET /rest/api/3/version/{id}/relatedwork` — Get related work

- Request: [[Jira v3 - Get related work]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
