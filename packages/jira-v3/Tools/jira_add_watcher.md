---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-watchers
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_add_watcher
title: "Jira v3 - Add watcher"
kind: request
request: "[[Jira v3 - Add watcher]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issue/{issueIdOrKey}/watchers · Add watcher. Adds a user as a watcher of an issue by passing the account ID of the user. For example, \"5b10ac8d82e05b22cc7d4ef5\". If no user is specified the calling user is added. This operation requires the Allow users to watch issues option to be ON. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_add_watcher

`POST /rest/api/3/issue/{issueIdOrKey}/watchers` — Add watcher

- Request: [[Jira v3 - Add watcher]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
