---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_create_related_work
title: "Jira v3 - Create related work"
kind: request
request: "[[Jira v3 - Create related work]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/version/{id}/relatedwork · Create related work. Creates a related work for the given version. You can only create a generic link type of related works via this API. relatedWorkId will be auto-generated UUID, that does not need to be provided. This operation can be accessed anonymously. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_related_work

`POST /rest/api/3/version/{id}/relatedwork` — Create related work

- Request: [[Jira v3 - Create related work]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
