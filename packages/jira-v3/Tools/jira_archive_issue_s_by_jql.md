---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_archive_issue_s_by_jql
title: "Jira v3 - Archive issue(s) by JQL"
kind: request
request: "[[Jira v3 - Archive issue(s) by JQL]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issue/archive · Archive issue(s) by JQL. Enables admins to archive up to 100,000 issues in a single request using JQL, returning the URL to check the status of the submitted request. You can use the get task and cancel task APIs to manage the request. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_archive_issue_s_by_jql

`POST /rest/api/3/issue/archive` — Archive issue(s) by JQL

- Request: [[Jira v3 - Archive issue(s) by JQL]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
