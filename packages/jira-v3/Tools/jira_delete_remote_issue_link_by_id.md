---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-remote-links
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_remote_issue_link_by_id
title: "Jira v3 - Delete remote issue link by ID"
kind: request
request: "[[Jira v3 - Delete remote issue link by ID]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId} · Delete remote issue link by ID. Deletes a remote issue link from an issue. This operation requires issue linking to be active. This operation can be accessed anonymously. Permissions required: Browse projects, Edit issues, and Link issues project permission for the project that the issue is in. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "linkId":
    type: string
    required: true
    description: "The ID of a remote issue link."
writes: true
expose: false
---
# jira_delete_remote_issue_link_by_id

`DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}` — Delete remote issue link by ID

- Request: [[Jira v3 - Delete remote issue link by ID]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
