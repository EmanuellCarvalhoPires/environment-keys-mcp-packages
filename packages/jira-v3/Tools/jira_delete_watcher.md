---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-watchers
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_watcher
title: "Jira v3 - Delete watcher"
kind: request
request: "[[Jira v3 - Delete watcher]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issue/{issueIdOrKey}/watchers · Delete watcher. Deletes a user as a watcher of an issue. This operation requires the Allow users to watch issues option to be ON. This option is set in General configuration for Jira. See Configuring Jira application options for details. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "username":
    type: string
    required: false
    description: "This parameter is no longer available. See the deprecation notice for details."
  "accountId":
    type: string
    required: false
    description: "The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5. Required."
writes: true
expose: false
---
# jira_delete_watcher

`DELETE /rest/api/3/issue/{issueIdOrKey}/watchers` — Delete watcher

- Request: [[Jira v3 - Delete watcher]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
