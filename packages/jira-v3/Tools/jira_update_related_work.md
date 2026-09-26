---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_update_related_work
title: "Jira v3 - Update related work"
kind: request
request: "[[Jira v3 - Update related work]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/version/{id}/relatedwork · Update related work. Updates the given related work. You can only update generic link related works via Rest APIs. Any archived version related works can't be edited. This operation can be accessed anonymously. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the version to update the related work on. For the related work id, pass it to the input JSON."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_related_work

`PUT /rest/api/3/version/{id}/relatedwork` — Update related work

- Request: [[Jira v3 - Update related work]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
