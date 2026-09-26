---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-remote-links
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}"
category: "Issue remote links"
writes_data: true
tool_note: "[[jira_delete_remote_issue_link_by_id]]"
---
# Jira v3 - Delete remote issue link by ID

**Delete remote issue link by ID** — `DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}`

- Run by the tool [[jira_delete_remote_issue_link_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/remotelink/{{param:linkId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `linkId` (path, string, required) — The ID of a remote issue link.

## Original description

Deletes a remote issue link from an issue.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects*, *Edit issues*, and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
