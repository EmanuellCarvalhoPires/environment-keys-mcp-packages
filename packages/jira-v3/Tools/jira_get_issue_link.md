---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-links
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_link
title: "Jira v3 - Get issue link"
kind: request
request: "[[Jira v3 - Get issue link]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issueLink/{linkId} · Get issue link. Returns an issue link. This operation can be accessed anonymously. Permissions required: Browse project project permission for all the projects containing the linked issues. If issue-level security is configured, permission to view both of the issues. Writes data: no."
params:
  "linkId":
    type: string
    required: true
    description: "The ID of the issue link."
writes: false
expose: false
---
# jira_get_issue_link

`GET /rest/api/3/issueLink/{linkId}` — Get issue link

- Request: [[Jira v3 - Get issue link]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
