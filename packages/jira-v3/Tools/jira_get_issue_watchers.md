---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-watchers
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_watchers
title: "Jira v3 - Get issue watchers"
kind: request
request: "[[Jira v3 - Get issue watchers]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/{issueIdOrKey}/watchers · Get issue watchers. Returns the watchers for an issue. This operation requires the Allow users to watch issues option to be ON. This option is set in General configuration for Jira. See Configuring Jira application options for details. This operation can be accessed anonymously. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
writes: false
expose: false
---
# jira_get_issue_watchers

`GET /rest/api/3/issue/{issueIdOrKey}/watchers` — Get issue watchers

- Request: [[Jira v3 - Get issue watchers]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
