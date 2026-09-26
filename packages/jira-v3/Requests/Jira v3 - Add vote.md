---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-votes
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issue/{issueIdOrKey}/votes"
category: "Issue votes"
writes_data: true
tool_note: "[[jira_add_vote]]"
---
# Jira v3 - Add vote

**Add vote** — `POST /rest/api/3/issue/{issueIdOrKey}/votes`

- Run by the tool [[jira_add_vote]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/votes
Authorization: {{service.auth_token}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.

## Original description

Adds the user's vote to an issue. This is the equivalent of the user clicking *Vote* on an issue in Jira.

This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
