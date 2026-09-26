---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-remote-links
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_remote_issue_links
title: "Jira v3 - Get remote issue links"
kind: request
request: "[[Jira v3 - Get remote issue links]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/{issueIdOrKey}/remotelink · Get remote issue links. Returns the remote issue links for an issue. When a remote issue link global ID is provided the record with that global ID is returned, otherwise all remote issue links are returned. Where a global ID includes reserved URL characters these must be escaped in the request. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "globalId":
    type: string
    required: false
    description: "The global ID of the remote issue link."
writes: false
expose: false
---
# jira_get_remote_issue_links

`GET /rest/api/3/issue/{issueIdOrKey}/remotelink` — Get remote issue links

- Request: [[Jira v3 - Get remote issue links]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
