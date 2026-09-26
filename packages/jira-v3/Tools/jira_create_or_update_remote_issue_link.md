---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-remote-links
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_create_or_update_remote_issue_link
title: "Jira v3 - Create or update remote issue link"
kind: request
request: "[[Jira v3 - Create or update remote issue link]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issue/{issueIdOrKey}/remotelink · Create or update remote issue link. Creates or updates a remote issue link for an issue. If a globalId is provided and a remote issue link with that global ID is found it is updated. Any fields without values in the request are set to null. Otherwise, the remote issue link is created. Writes data: yes."
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
# jira_create_or_update_remote_issue_link

`POST /rest/api/3/issue/{issueIdOrKey}/remotelink` — Create or update remote issue link

- Request: [[Jira v3 - Create or update remote issue link]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
