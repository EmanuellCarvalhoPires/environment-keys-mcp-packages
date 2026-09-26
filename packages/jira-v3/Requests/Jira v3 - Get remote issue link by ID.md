---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-remote-links
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}"
category: "Issue remote links"
writes_data: false
tool_note: "[[jira_get_remote_issue_link_by_id]]"
---
# Jira v3 - Get remote issue link by ID

**Get remote issue link by ID** — `GET /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}`

- Run by the tool [[jira_get_remote_issue_link_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/remotelink/{{param:linkId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `linkId` (path, string, required) — The ID of the remote issue link.

## Original description

Returns a remote issue link for an issue.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
