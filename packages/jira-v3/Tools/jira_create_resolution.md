---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-resolutions
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_resolution
title: "Jira v3 - Create resolution"
kind: request
request: "[[Jira v3 - Create resolution]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/resolution · Create resolution. Creates an issue resolution. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_resolution

`POST /rest/api/3/resolution` — Create resolution

- Request: [[Jira v3 - Create resolution]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
