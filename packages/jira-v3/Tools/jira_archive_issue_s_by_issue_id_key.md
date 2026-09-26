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
tool: jira_archive_issue_s_by_issue_id_key
title: "Jira v3 - Archive issue(s) by issue ID key"
kind: request
request: "[[Jira v3 - Archive issue(s) by issue ID key]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issue/archive · Archive issue(s) by issue ID/key. Enables admins to archive up to 1000 issues in a single request using issue ID/key, returning details of the issue(s) archived in the process and the errors encountered, if any. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_archive_issue_s_by_issue_id_key

`PUT /rest/api/3/issue/archive` — Archive issue(s) by issue ID/key

- Request: [[Jira v3 - Archive issue(s) by issue ID key]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
