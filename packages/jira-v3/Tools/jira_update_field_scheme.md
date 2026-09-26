---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_field_scheme
title: "Jira v3 - Update field scheme"
kind: request
request: "[[Jira v3 - Update field scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/config/fieldschemes/{id} · Update field scheme. Endpoint for updating an existing field association scheme. Permissions required: Administer Jira global permission. Writes data: yes."
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
# jira_update_field_scheme

`PUT /rest/api/3/config/fieldschemes/{id}` — Update field scheme

- Request: [[Jira v3 - Update field scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
