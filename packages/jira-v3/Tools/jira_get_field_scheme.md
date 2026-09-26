---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/field-schemes
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_field_scheme
title: "Jira v3 - Get field scheme"
kind: request
request: "[[Jira v3 - Get field scheme]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/config/fieldschemes/{id} · Get field scheme. Endpoint for fetching a field association scheme by its ID Permissions required: Administer Jira global permission. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The scheme id to fetch"
writes: false
expose: false
---
# jira_get_field_scheme

`GET /rest/api/3/config/fieldschemes/{id}` — Get field scheme

- Request: [[Jira v3 - Get field scheme]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
