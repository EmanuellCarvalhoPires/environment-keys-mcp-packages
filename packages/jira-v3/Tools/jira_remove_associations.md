---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-associations
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_remove_associations
title: "Jira v3 - Remove associations"
kind: request
request: "[[Jira v3 - Remove associations]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/field/association · Remove associations. Unassociates a set of fields with a project and issue type context. Fields will be unassociated with all projects/issue types that share the same field configuration which the provided project and issue types are using. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_remove_associations

`DELETE /rest/api/3/field/association` — Remove associations

- Request: [[Jira v3 - Remove associations]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
