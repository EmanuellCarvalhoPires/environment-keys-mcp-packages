---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklogs
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/issue/{issueIdOrKey}/worklog"
category: "Issue worklogs"
writes_data: true
tool_note: "[[jira_bulk_delete_worklogs]]"
---
# Jira v3 - Bulk delete worklogs

**Bulk delete worklogs** — `DELETE /rest/api/3/issue/{issueIdOrKey}/worklog`

- Run by the tool [[jira_bulk_delete_worklogs]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/worklog?adjustEstimate={{param:adjustEstimate}}&overrideEditableFlag={{param:overrideEditableFlag}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `adjustEstimate` (query, string, optional) — Defines how to update the issue's time estimate, the options are: leave Leaves the estimate unchanged. auto Reduces the estimate by the aggregate value of timeSpent across all worklogs being deleted.
- `overrideEditableFlag` (query, string, optional) — Whether the work log entries should be removed to the issue even if the issue is not editable, because jira.issue.editable set to false or missing. For example, the issue is closed.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "ids": [
    1,
    2,
    5,
    10
  ]
}
```

## Original description

Deletes a list of worklogs from an issue. This is an experimental API with limitations:

 *  You can't delete more than 5000 worklogs at once.
 *  No notifications will be sent for deleted worklogs.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  *Delete all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete any worklog.
 *  If any worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
