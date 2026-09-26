---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_change_filter_owner
title: "Jira v3 - Change filter owner"
kind: request
request: "[[Jira v3 - Change filter owner]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/filter/{id}/owner · Change filter owner. Changes the owner of the filter. Permissions required: Permission to access Jira. However, the user must own the filter or have the Administer Jira global permission. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the filter to update."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_change_filter_owner

`PUT /rest/api/3/filter/{id}/owner` — Change filter owner

- Request: [[Jira v3 - Change filter owner]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
