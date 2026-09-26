---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comments
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_update_comment
title: "Jira v3 - Update comment"
kind: request
request: "[[Jira v3 - Update comment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/issue/{issueIdOrKey}/comment/{id} · Update comment. Updates a comment. This operation can be accessed anonymously. Permissions required: Browse projects project permission for the project that the issue containing the comment is in. If issue-level security is configured, issue-level security permission to view the issue. Writes data: yes."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "id":
    type: string
    required: true
    description: "The ID of the comment."
  "notifyUsers":
    type: string
    required: false
    description: "Whether users are notified when a comment is updated."
  "overrideEditableFlag":
    type: string
    required: false
    description: "Whether screen security is overridden to enable uneditable fields to be edited. Available to Connect app users with the Administer Jira global permission and Forge apps acting on behalf of users with…"
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about comments in the response. This parameter accepts renderedBody, which returns the comment body rendered in HTML."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_comment

`PUT /rest/api/3/issue/{issueIdOrKey}/comment/{id}` — Update comment

- Request: [[Jira v3 - Update comment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
