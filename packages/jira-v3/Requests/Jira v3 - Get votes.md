---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-votes
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/{issueIdOrKey}/votes"
category: "Issue votes"
writes_data: false
tool_note: "[[jira_get_votes]]"
---
# Jira v3 - Get votes

**Get votes** — `GET /rest/api/3/issue/{issueIdOrKey}/votes`

- Run by the tool [[jira_get_votes]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/votes
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.

## Original description

Returns details about the votes on an issue.

This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is ini
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Note that users with the necessary permissions for this operation but without the *View voters and watchers* project permissions are not returned details in the `voters` field.
