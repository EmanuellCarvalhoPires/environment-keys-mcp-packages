---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-votes
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_vote
title: "Jira v3 - Delete vote"
kind: request
request: "[[Jira v3 - Delete vote]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/issue/{issueIdOrKey}/votes · Delete vote. Deletes a user's vote from an issue. This is the equivalent of the user clicking Unvote on an issue in Jira. This operation requires the Allow users to vote on issues option to be ON. This option is set in General configuration for Jira. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
writes: true
expose: false
---
# jira_delete_vote

`DELETE /rest/api/3/issue/{issueIdOrKey}/votes` — Delete vote

- Request: [[Jira v3 - Delete vote]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
