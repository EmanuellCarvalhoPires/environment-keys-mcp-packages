---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-resolutions
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_set_default_resolution
title: "Jira v3 - Set default resolution"
kind: request
request: "[[Jira v3 - Set default resolution]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/resolution/default · Set default resolution. Sets default issue resolution. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_default_resolution

`PUT /rest/api/3/resolution/default` — Set default resolution

- Request: [[Jira v3 - Set default resolution]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
