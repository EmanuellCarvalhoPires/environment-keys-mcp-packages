---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comments
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/comment/list"
category: "Issue comments"
writes_data: false
tool_note: "[[jira_get_comments_by_ids]]"
---
# Jira v3 - Get comments by IDs

**Get comments by IDs** — `POST /rest/api/3/comment/list`

- Run by the tool [[jira_get_comments_by_ids]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/comment/list?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `expand` (query, string, optional) — Use expand to include additional information about comments in the response. This parameter accepts a comma-separated list.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "ids": [
    1,
    2,
    5,
    10
  ]
}
```

## Original description

Returns a [paginated](#pagination) list of comments specified by a list of comment IDs.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Comments are returned where the user:

 *  has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the comment.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.
