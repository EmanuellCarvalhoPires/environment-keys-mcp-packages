---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-links
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_issue_link
title: "Jira v3 - Delete issue link"
kind: request
request: "[[Jira v3 - Delete issue link]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issueLink/{linkId} · Delete issue link. Deletes an issue link. This operation can be accessed anonymously. Permissions required: Browse project project permission for all the projects containing the issues in the link. Link issues project permission for at least one of the projects containing issues in the link. Writes data: yes."
params:
  "linkId":
    type: string
    required: true
    description: "The ID of the issue link."
writes: true
expose: false
---
# jira_delete_issue_link

`DELETE /rest/api/3/issueLink/{linkId}` — Delete issue link

- Request: [[Jira v3 - Delete issue link]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
