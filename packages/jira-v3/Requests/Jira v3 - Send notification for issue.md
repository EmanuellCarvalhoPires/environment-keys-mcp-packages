---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issue/{issueIdOrKey}/notify"
category: "Issues"
writes_data: true
tool_note: "[[jira_send_notification_for_issue]]"
---
# Jira v3 - Send notification for issue

**Send notification for issue** — `POST /rest/api/3/issue/{issueIdOrKey}/notify`

- Run by the tool [[jira_send_notification_for_issue]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/notify
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — ID or key of the issue that the notification is sent for.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "htmlBody": "The <strong>latest</strong> test results for this ticket are now available.",
  "restrict": {
    "groupIds": [],
    "groups": [
      {
        "name": "notification-group"
      }
    ],
    "permissions": [
      {
        "key": "BROWSE"
      }
    ]
  },
  "subject": "Latest test results",
  "textBody": "The latest test results for this ticket are now available.",
  "to": {
    "assignee": false,
    "groupIds": [],
    "groups": [
      {
        "name": "notification-group"
      }
    ],
    "reporter": false,
    "users": [
      {
        "accountId": "5b10a2844c20165700ede21g",
        "active": false
      }
    ],
    "voters": true,
    "watchers": true
  }
}
```

## Original description

Creates an email notification for an issue and adds it to the mail queue.

**[Permissions](#permissions) required:**

 *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
