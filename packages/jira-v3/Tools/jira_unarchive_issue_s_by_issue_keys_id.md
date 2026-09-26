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
tool: jira_unarchive_issue_s_by_issue_keys_id
title: "Jira v3 - Unarchive issue(s) by issue keys ID"
kind: request
request: "[[Jira v3 - Unarchive issue(s) by issue keys ID]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issue/unarchive · Unarchive issue(s) by issue keys/ID. Enables admins to unarchive up to 1000 issues in a single request using issue ID/key, returning details of the issue(s) unarchived in the process and the errors encountered, if any. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_unarchive_issue_s_by_issue_keys_id

`PUT /rest/api/3/issue/unarchive` — Unarchive issue(s) by issue keys/ID

- Request: [[Jira v3 - Unarchive issue(s) by issue keys ID]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
