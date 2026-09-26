---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklogs
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issue/{issueIdOrKey}/worklog/move"
category: "Issue worklogs"
writes_data: true
tool_note: "[[jira_bulk_move_worklogs]]"
---
# Jira v3 - Bulk move worklogs

**Bulk move worklogs** — `POST /rest/api/3/issue/{issueIdOrKey}/worklog/move`

- Run by the tool [[jira_bulk_move_worklogs]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/worklog/move?adjustEstimate={{param:adjustEstimate}}&overrideEditableFlag={{param:overrideEditableFlag}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — Value of issueIdOrKey in the path.
- `adjustEstimate` (query, string, optional) — Defines how to update the issues' time estimate, the options are: leave Leaves the estimate unchanged.
- `overrideEditableFlag` (query, string, optional) — Whether the work log entry should be moved to and from the issues even if the issues are not editable, because jira.issue.editable set to false or missing. For example, the issue is closed.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "ids": [
    1,
    2,
    5,
    10
  ],
  "issueIdOrKey": "ABC-1234"
}
```

## Original description

Moves a list of worklogs from one issue to another. This is an experimental API with several limitations:

 *  You can't move more than 5000 worklogs at once.
 *  You can't move worklogs containing an attachment.
 *  You can't move worklogs restricted by project roles.
 *  No notifications will be sent for moved worklogs.
 *  No webhooks or events will be sent for moved worklogs.
 *  No issue history will be recorded for moved worklogs.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the projects containing the source and destination issues.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  *Delete all worklogs* [project permission](https://confluence.atlassian.com/x/yodKLg)
 *  *Work on issues* [project permission](https://confluence.atlassian.com/x/yodKLg) to log work on an issue, that is to create a worklog entry, if time tracking is enabled. This permission is required as a prerequisite for applying the other time-tracking permissions
 *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
