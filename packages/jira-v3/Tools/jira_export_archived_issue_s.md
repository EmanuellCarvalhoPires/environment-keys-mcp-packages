---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_export_archived_issue_s
title: "Jira v3 - Export archived issue(s)"
kind: request
request: "[[Jira v3 - Export archived issue(s)]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issues/archive/export · Export archived issue(s). Enables admins to retrieve details of all archived issues. Upon a successful request, the admin who submitted it will receive an email with a link to download a CSV file with the issue details. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_export_archived_issue_s

`PUT /rest/api/3/issues/archive/export` — Export archived issue(s)

- Request: [[Jira v3 - Export archived issue(s)]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
