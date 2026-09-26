---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-remote-links
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/{issueIdOrKey}/remotelink"
category: "Issue remote links"
writes_data: false
tool_note: "[[jira_get_remote_issue_links]]"
---
# Jira v3 - Get remote issue links

**Get remote issue links** — `GET /rest/api/3/issue/{issueIdOrKey}/remotelink`

- Run by the tool [[jira_get_remote_issue_links]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/remotelink?globalId={{param:globalId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `globalId` (query, string, optional) — The global ID of the remote issue link.

## Original description

Returns the remote issue links for an issue. When a remote issue link global ID is provided the record with that global ID is returned, otherwise all remote issue links are returned. Where a global ID includes reserved URL characters these must be escaped in the request. For example, pass `system=http://www.mycompany.com/support&id=1` as `system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
