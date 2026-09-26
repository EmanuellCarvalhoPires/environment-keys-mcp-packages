---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_and_replace_version
title: "Jira v3 - Delete and replace version"
kind: request
request: "[[Jira v3 - Delete and replace version]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/version/{id}/removeAndSwap · Delete and replace version. Deletes a project version. Alternative versions can be provided to update issues that use the deleted version in fixVersion, affectedVersion, or any version picker custom fields. Writes data: yes."
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
# jira_delete_and_replace_version

`POST /rest/api/3/version/{id}/removeAndSwap` — Delete and replace version

- Request: [[Jira v3 - Delete and replace version]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
