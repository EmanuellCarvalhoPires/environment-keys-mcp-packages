---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-remote-links
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issue/{issueIdOrKey}/remotelink"
category: "Issue remote links"
writes_data: true
tool_note: "[[jira_create_or_update_remote_issue_link]]"
---
# Jira v3 - Create or update remote issue link

**Create or update remote issue link** — `POST /rest/api/3/issue/{issueIdOrKey}/remotelink`

- Run by the tool [[jira_create_or_update_remote_issue_link]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/remotelink
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "application": {
    "name": "My Acme Tracker",
    "type": "com.acme.tracker"
  },
  "globalId": "system=http://www.mycompany.com/support&id=1",
  "object": {
    "icon": {
      "title": "Support Ticket",
      "url16x16": "http://www.mycompany.com/support/ticket.png"
    },
    "status": {
      "icon": {
        "link": "http://www.mycompany.com/support?id=1&details=closed",
        "title": "Case Closed",
        "url16x16": "http://www.mycompany.com/support/resolved.png"
      },
      "resolved": true
    },
    "summary": "Customer support issue",
    "title": "TSTSUP-111",
    "url": "http://www.mycompany.com/support?id=1"
  },
  "relationship": "causes"
}
```

## Original description

Creates or updates a remote issue link for an issue.

If a `globalId` is provided and a remote issue link with that global ID is found it is updated. Any fields without values in the request are set to null. Otherwise, the remote issue link is created.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
