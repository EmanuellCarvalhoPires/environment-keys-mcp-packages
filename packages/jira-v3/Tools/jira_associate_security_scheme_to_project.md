---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_associate_security_scheme_to_project
title: "Jira v3 - Associate security scheme to project"
kind: request
request: "[[Jira v3 - Associate security scheme to project]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issuesecurityschemes/project · Associate security scheme to project. Associates an issue security scheme with a project and remaps security levels of issues to the new levels, if provided. This operation is asynchronous. Follow the location link in the response to determine the status of the task and use Get task to obtain subsequent updates. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_associate_security_scheme_to_project

`PUT /rest/api/3/issuesecurityschemes/project` — Associate security scheme to project

- Request: [[Jira v3 - Associate security scheme to project]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
