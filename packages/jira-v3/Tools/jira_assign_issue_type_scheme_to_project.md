---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_assign_issue_type_scheme_to_project
title: "Jira v3 - Assign issue type scheme to project"
kind: request
request: "[[Jira v3 - Assign issue type scheme to project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issuetypescheme/project · Assign issue type scheme to project. Assigns an issue type scheme to a project. If any issues in the project are assigned issue types not present in the new scheme, the operation will fail. To complete the assignment those issues must be updated to use issue types in the new scheme. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_assign_issue_type_scheme_to_project

`PUT /rest/api/3/issuetypescheme/project` — Assign issue type scheme to project

- Request: [[Jira v3 - Assign issue type scheme to project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
