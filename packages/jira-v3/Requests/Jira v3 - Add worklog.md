---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklogs
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issue/{issueIdOrKey}/worklog"
category: "Issue worklogs"
writes_data: true
tool_note: "[[jira_add_worklog]]"
---
# Jira v3 - Add worklog

**Add worklog** — `POST /rest/api/3/issue/{issueIdOrKey}/worklog`

- Run by the tool [[jira_add_worklog]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/worklog?notifyUsers={{param:notifyUsers}}&adjustEstimate={{param:adjustEstimate}}&newEstimate={{param:newEstimate}}&reduceBy={{param:reduceBy}}&expand={{param:expand}}&overrideEditableFlag={{param:overrideEditableFlag}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key the issue.
- `notifyUsers` (query, string, optional) — Whether users watching the issue are notified by email.
- `adjustEstimate` (query, string, optional) — Defines how to update the issue's time estimate, the options are: new Sets the estimate to a specific value, defined in newEstimate. leave Leaves the estimate unchanged.
- `newEstimate` (query, string, optional) — The value to set as the issue's remaining time estimate, as days (\d), hours (\h), or minutes (\m or \). For example, 2d. Required when adjustEstimate is new.
- `reduceBy` (query, string, optional) — The amount to reduce the issue's remaining estimate by, as days (\d), hours (\h), or minutes (\m). For example, 2d. Required when adjustEstimate is manual.
- `expand` (query, string, optional) — Use expand to include additional information about work logs in the response. This parameter accepts properties, which returns worklog properties.
- `overrideEditableFlag` (query, string, optional) — Whether the worklog entry should be added to the issue even if the issue is not editable, because jira.issue.editable set to false or missing. For example, the issue is closed.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "comment": {
    "content": [
      {
        "content": [
          {
            "text": "I did some work here.",
            "type": "text"
          }
        ],
        "type": "paragraph"
      }
    ],
    "type": "doc",
    "version": 1
  },
  "started": "2021-01-17T12:34:00.000+0000",
  "timeSpentSeconds": 12000,
  "visibility": {
    "identifier": "276f955c-63d7-42c8-9520-92d01dca0625",
    "type": "group"
  }
}
```

## Original description

Adds a worklog to an issue.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Work on issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
