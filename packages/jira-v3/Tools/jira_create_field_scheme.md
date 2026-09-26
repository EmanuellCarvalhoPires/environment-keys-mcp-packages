---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_field_scheme
title: "Jira v3 - Create field scheme"
kind: request
request: "[[Jira v3 - Create field scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/config/fieldschemes · Create field scheme. Endpoint for creating a new field association scheme. A new scheme is not copied from, or based on, any existing field association scheme. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_field_scheme

`POST /rest/api/3/config/fieldschemes` — Create field scheme

- Request: [[Jira v3 - Create field scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
