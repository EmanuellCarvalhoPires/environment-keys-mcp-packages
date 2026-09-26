---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-associations
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_create_associations
title: "Jira v3 - Create associations"
kind: request
request: "[[Jira v3 - Create associations]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/field/association · Create associations. Associates fields with projects. Fields will be associated with each issue type on the requested projects. Fields will be associated with all projects that share the same field configuration which the provided projects are using. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_associations

`PUT /rest/api/3/field/association` — Create associations

- Request: [[Jira v3 - Create associations]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
