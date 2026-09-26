---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-components
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_component
title: "Jira v3 - Delete component"
kind: request
request: "[[Jira v3 - Delete component]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/component/{id} · Delete component. Deletes a component. This operation can be accessed anonymously. Permissions required: Administer projects project permission for the project containing the component or Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the component."
  "moveIssuesTo":
    type: string
    required: false
    description: "The ID of the component to replace the deleted component. If this value is null no replacement is made."
writes: true
expose: false
---
# jira_delete_component

`DELETE /rest/api/3/component/{id}` — Delete component

- Request: [[Jira v3 - Delete component]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
