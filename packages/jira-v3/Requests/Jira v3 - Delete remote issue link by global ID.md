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
path: "/rest/api/3/issue/{issueIdOrKey}/remotelink"
category: "Issue remote links"
writes_data: true
tool_note: "[[jira_delete_remote_issue_link_by_global_id]]"
---
# Jira v3 - Delete remote issue link by global ID

**Delete remote issue link by global ID** — `DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink`

- Run by the tool [[jira_delete_remote_issue_link_by_global_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/remotelink?globalId={{param:globalId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `globalId` (query, string, required) — The global ID of a remote issue link.

## Original description

Deletes the remote issue link from the issue using the link's global ID. Where the global ID includes reserved URL characters these must be escaped in the request. For example, pass `system=http://www.mycompany.com/support&id=1` as `system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is implemented, issue-level security permission to view the issue.
