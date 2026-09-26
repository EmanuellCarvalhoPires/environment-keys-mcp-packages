---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-remote-links
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_remote_issue_link_by_id
title: "Jira v3 - Get remote issue link by ID"
kind: request
request: "[[Jira v3 - Get remote issue link by ID]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId} · Get remote issue link by ID. Returns a remote issue link for an issue. This operation requires issue linking to be active. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project that the issue is in. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "linkId":
    type: string
    required: true
    description: "The ID of the remote issue link."
writes: false
expose: false
---
# jira_get_remote_issue_link_by_id

`GET /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}` — Get remote issue link by ID

- Request: [[Jira v3 - Get remote issue link by ID]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
