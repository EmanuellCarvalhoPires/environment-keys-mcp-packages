---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comment-properties
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_delete_comment_property
title: "Jira v3 - Delete comment property"
kind: request
request: "[[Jira v3 - Delete comment property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/comment/{commentId}/properties/{propertyKey} · Delete comment property. Deletes a comment property. Permissions required: either of: Edit All Comments project permission to delete a property from any comment. Edit Own Comments project permission to delete a property from a comment created by the user. Writes data: yes."
params:
  "commentId":
    type: string
    required: true
    description: "The ID of the comment."
  "propertyKey":
    type: string
    required: true
    description: "The key of the property."
writes: true
expose: false
---
# jira_delete_comment_property

`DELETE /rest/api/3/comment/{commentId}/properties/{propertyKey}` — Delete comment property

- Request: [[Jira v3 - Delete comment property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
