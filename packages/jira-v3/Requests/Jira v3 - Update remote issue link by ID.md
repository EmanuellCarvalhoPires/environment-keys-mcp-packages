---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-remote-links
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}"
category: "Issue remote links"
writes_data: true
tool_note: "[[jira_update_remote_issue_link_by_id]]"
---
# Jira v3 - Update remote issue link by ID

**Update remote issue link by ID** — `PUT /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}`

- Run by the tool [[jira_update_remote_issue_link_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/remotelink/{{param:linkId}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `linkId` (path, string, required) — The ID of the remote issue link.
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

Updates a remote issue link for an issue.

Note: Fields without values in the request are set to null.

This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
