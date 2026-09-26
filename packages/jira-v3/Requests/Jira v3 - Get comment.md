---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comments
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/{issueIdOrKey}/comment/{id}"
category: "Issue comments"
writes_data: false
tool_note: "[[jira_get_comment]]"
---
# Jira v3 - Get comment

**Get comment** — `GET /rest/api/3/issue/{issueIdOrKey}/comment/{id}`

- Run by the tool [[jira_get_comment]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/comment/{{param:id}}?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `id` (path, string, required) — The ID of the comment.
- `expand` (query, string, optional) — Use expand to include additional information about comments in the response. This parameter accepts renderedBody, which returns the comment body rendered in HTML.

## Original description

Returns a comment.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the comment.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the comment has visibility restrictions, the user belongs to the group or has the role visibility is restricted to.
