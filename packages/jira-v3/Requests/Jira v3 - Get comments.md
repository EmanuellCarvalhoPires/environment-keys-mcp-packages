---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comments
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/{issueIdOrKey}/comment"
category: "Issue comments"
writes_data: false
tool_note: "[[jira_get_comments]]"
---
# Jira v3 - Get comments

**Get comments** — `GET /rest/api/3/issue/{issueIdOrKey}/comment`

- Run by the tool [[jira_get_comments]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/comment?startAt={{param:startAt}}&maxResults={{param:maxResults}}&orderBy={{param:orderBy}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `orderBy` (query, string, optional) — Order the results by a field. Accepts created to sort comments by their created date.
- `expand` (query, string, optional) — Use expand to include additional information about comments in the response. This parameter accepts renderedBody, which returns the comment body rendered in HTML.

## Original description

Returns all comments for an issue.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Comments are included in the response where the user has:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the comment.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the comment has visibility restrictions, belongs to the group or has the role visibility is role visibility is restricted to.
