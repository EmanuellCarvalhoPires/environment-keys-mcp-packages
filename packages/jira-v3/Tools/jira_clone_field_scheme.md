---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_clone_field_scheme
title: "Jira v3 - Clone field scheme"
kind: request
request: "[[Jira v3 - Clone field scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/config/fieldschemes/{id}/clone · Clone field scheme. Endpoint for cloning an existing field association scheme into a new one. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the source field association scheme to clone from"
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_clone_field_scheme

`POST /rest/api/3/config/fieldschemes/{id}/clone` — Clone field scheme

- Request: [[Jira v3 - Clone field scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
