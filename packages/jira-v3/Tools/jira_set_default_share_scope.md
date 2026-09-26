---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filter-sharing
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_set_default_share_scope
title: "Jira v3 - Set default share scope"
kind: request
request: "[[Jira v3 - Set default share scope]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/filter/defaultShareScope · Set default share scope. Sets the default sharing for new filters and dashboards for a user. Permissions required: Permission to access Jira. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_default_share_scope

`PUT /rest/api/3/filter/defaultShareScope` — Set default share scope

- Request: [[Jira v3 - Set default share scope]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
