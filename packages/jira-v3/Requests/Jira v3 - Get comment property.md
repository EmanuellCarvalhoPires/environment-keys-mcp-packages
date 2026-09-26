---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comment-properties
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/comment/{commentId}/properties/{propertyKey}"
category: "Issue comment properties"
writes_data: false
tool_note: "[[jira_get_comment_property]]"
---
# Jira v3 - Get comment property

**Get comment property** — `GET /rest/api/3/comment/{commentId}/properties/{propertyKey}`

- Run by the tool [[jira_get_comment_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/comment/{{param:commentId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `commentId` (path, string, required) — The ID of the comment.
- `propertyKey` (path, string, required) — The key of the property.

## Original description

Returns the value of a comment property.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.
