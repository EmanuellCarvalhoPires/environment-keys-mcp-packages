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
path: "/rest/api/3/issue/{issueIdOrKey}/worklog/{id}"
category: "Issue worklogs"
writes_data: true
tool_note: "[[jira_delete_worklog]]"
---
# Jira v3 - Delete worklog

**Delete worklog** — `DELETE /rest/api/3/issue/{issueIdOrKey}/worklog/{id}`

- Run by the tool [[jira_delete_worklog]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/worklog/{{param:id}}?notifyUsers={{param:notifyUsers}}&adjustEstimate={{param:adjustEstimate}}&newEstimate={{param:newEstimate}}&increaseBy={{param:increaseBy}}&overrideEditableFlag={{param:overrideEditableFlag}}
Authorization: {{service.auth_token}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `id` (path, string, required) — The ID of the worklog.
- `notifyUsers` (query, string, optional) — Whether users watching the issue are notified by email.
- `adjustEstimate` (query, string, optional) — Defines how to update the issue's time estimate, the options are: new Sets the estimate to a specific value, defined in newEstimate. leave Leaves the estimate unchanged.
- `newEstimate` (query, string, optional) — The value to set as the issue's remaining time estimate, as days (\d), hours (\h), or minutes (\m or \). For example, 2d. Required when adjustEstimate is new.
- `increaseBy` (query, string, optional) — The amount to increase the issue's remaining estimate by, as days (\d), hours (\h), or minutes (\m or \). For example, 2d. Required when adjustEstimate is manual.
- `overrideEditableFlag` (query, string, optional) — Whether the work log entry should be added to the issue even if the issue is not editable, because jira.issue.editable set to false or missing. For example, the issue is closed.

## Original description

Deletes a worklog from an issue.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  *Delete all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete any worklog or *Delete own worklogs* to delete worklogs created by the user,
 *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
