---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comments
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/issue/{issueIdOrKey}/comment/{id}"
category: "Issue comments"
writes_data: true
tool_note: "[[jira_delete_comment]]"
---
# Jira v3 - Delete comment

**Delete comment** — `DELETE /rest/api/3/issue/{issueIdOrKey}/comment/{id}`

- Run by the tool [[jira_delete_comment]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/comment/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `id` (path, string, required) — The ID of the comment.

## Original description

Deletes a comment.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue containing the comment is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  *Delete all comments*[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete any comment or *Delete own comments* to delete comment created by the user,
 *  If the comment has visibility restrictions, the user belongs to the group or has the role visibility is restricted to.
