---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_version
title: "Jira v3 - Update version"
kind: request
request: "[[Jira v3 - Update version]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/version/{id} · Update version. Updates a project version. This operation can be accessed anonymously. Permissions required: Administer Jira global permission or Administer Projects project permission for the project that contains the version. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the version."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_version

`PUT /rest/api/3/version/{id}` — Update version

- Request: [[Jira v3 - Update version]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
