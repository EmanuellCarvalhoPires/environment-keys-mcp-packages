---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-remote-links
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_update_remote_issue_link_by_id
title: "Jira v3 - Update remote issue link by ID"
kind: request
request: "[[Jira v3 - Update remote issue link by ID]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId} · Update remote issue link by ID. Updates a remote issue link for an issue. Note: Fields without values in the request are set to null. This operation requires issue linking to be active. This operation can be accessed anonymously. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "linkId":
    type: string
    required: true
    description: "The ID of the remote issue link."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_remote_issue_link_by_id

`PUT /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}` — Update remote issue link by ID

- Request: [[Jira v3 - Update remote issue link by ID]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
