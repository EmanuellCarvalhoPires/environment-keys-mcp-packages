---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-remote-links
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_remote_issue_link_by_global_id
title: "Jira v3 - Delete remote issue link by global ID"
kind: request
request: "[[Jira v3 - Delete remote issue link by global ID]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink · Delete remote issue link by global ID. Deletes the remote issue link from the issue using the link's global ID. Where the global ID includes reserved URL characters these must be escaped in the request. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "globalId":
    type: string
    required: true
    description: "The global ID of a remote issue link."
writes: true
expose: false
---
# jira_delete_remote_issue_link_by_global_id

`DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink` — Delete remote issue link by global ID

- Request: [[Jira v3 - Delete remote issue link by global ID]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
