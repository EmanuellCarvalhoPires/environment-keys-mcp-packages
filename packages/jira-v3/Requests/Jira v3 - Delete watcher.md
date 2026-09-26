---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-watchers
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/issue/{issueIdOrKey}/watchers"
category: "Issue watchers"
writes_data: true
tool_note: "[[jira_delete_watcher]]"
---
# Jira v3 - Delete watcher

**Delete watcher** — `DELETE /rest/api/3/issue/{issueIdOrKey}/watchers`

- Run by the tool [[jira_delete_watcher]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/watchers?username={{param:username}}&accountId={{param:accountId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `username` (query, string, optional) — This parameter is no longer available. See the deprecation notice for details.
- `accountId` (query, string, optional) — The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, 5b10ac8d82e05b22cc7d4ef5. Required.

## Original description

Deletes a user as a watcher of an issue.

This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  To remove users other than themselves from the watchlist, *Manage watcher list* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
