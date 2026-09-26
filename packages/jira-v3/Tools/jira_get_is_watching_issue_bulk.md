---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-watchers
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_is_watching_issue_bulk
title: "Jira v3 - Get is watching issue bulk"
kind: request
request: "[[Jira v3 - Get is watching issue bulk]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issue/watching · Get is watching issue bulk. Returns, for the user, details of the watched status of issues from a list. If an issue ID is invalid, the returned watched status is false. This operation requires the Allow users to watch issues option to be ON. This option is set in General configuration for Jira. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_get_is_watching_issue_bulk

`POST /rest/api/3/issue/watching` — Get is watching issue bulk

- Request: [[Jira v3 - Get is watching issue bulk]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
