---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-properties
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_set_project_property
title: "Jira v3 - Set project property"
kind: request
request: "[[Jira v3 - Set project property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey} · Set project property. Sets the value of the project property. You can use project properties to store custom data against the project. The value of the request body must be a valid, non-empty JSON blob. The maximum length is 32768 characters. This operation can be accessed anonymously. Writes data: yes."
params:
  "projectIdOrKey":
    type: string
    required: true
    description: "The project ID or project key (case sensitive)."
  "propertyKey":
    type: string
    required: true
    description: "The key of the project property. The maximum length is 255 characters."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_project_property

`PUT /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}` — Set project property

- Request: [[Jira v3 - Set project property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
