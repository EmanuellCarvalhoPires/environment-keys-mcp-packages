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
tool: jira_set_default_issue_security_levels
title: "Jira v3 - Set default issue security levels"
kind: request
request: "[[Jira v3 - Set default issue security levels]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issuesecurityschemes/level/default · Set default issue security levels. Sets default issue security levels for schemes. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_default_issue_security_levels

`PUT /rest/api/3/issuesecurityschemes/level/default` — Set default issue security levels

- Request: [[Jira v3 - Set default issue security levels]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
