---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-properties
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_delete_project_property
title: "Jira v3 - Delete project property"
kind: request
request: "[[Jira v3 - Delete project property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey} · Delete project property. Deletes the property from a project. This operation can be accessed anonymously. Permissions required: Administer Jira global permission or Administer Projects project permission for the project containing the property. Writes data: yes."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
  "propertyKey":
    type: string
    required: true
    description: "The project property key. Use Get project property keys to get a list of all project property keys."
writes: true
expose: false
---
# jira_delete_project_property

`DELETE /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}` — Delete project property

- Request: [[Jira v3 - Delete project property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
