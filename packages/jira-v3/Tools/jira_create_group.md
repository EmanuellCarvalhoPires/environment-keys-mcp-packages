---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/groups
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_group
title: "Jira v3 - Create group"
kind: request
request: "[[Jira v3 - Create group]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/group · Create group. Creates a group. Permissions required: Site administration (that is, member of the site-admin group). Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_group

`POST /rest/api/3/group` — Create group

- Request: [[Jira v3 - Create group]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
