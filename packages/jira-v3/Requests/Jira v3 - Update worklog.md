---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklogs
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issue/{issueIdOrKey}/worklog/{id}"
category: "Issue worklogs"
writes_data: true
tool_note: "[[jira_update_worklog]]"
---
# Jira v3 - Update worklog

**Update worklog** — `PUT /rest/api/3/issue/{issueIdOrKey}/worklog/{id}`

- Run by the tool [[jira_update_worklog]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/worklog/{{param:id}}?notifyUsers={{param:notifyUsers}}&adjustEstimate={{param:adjustEstimate}}&newEstimate={{param:newEstimate}}&expand={{param:expand}}&overrideEditableFlag={{param:overrideEditableFlag}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key the issue.
- `id` (path, string, required) — The ID of the worklog.
- `notifyUsers` (query, string, optional) — Whether users watching the issue are notified by email.
- `adjustEstimate` (query, string, optional) — Defines how to update the issue's time estimate, the options are: new Sets the estimate to a specific value, defined in newEstimate. leave Leaves the estimate unchanged.
- `newEstimate` (query, string, optional) — The value to set as the issue's remaining time estimate, as days (\d), hours (\h), or minutes (\m or \). For example, 2d. Required when adjustEstimate is new.
- `expand` (query, string, optional) — Use expand to include additional information about worklogs in the response. This parameter accepts properties, which returns worklog properties.
- `overrideEditableFlag` (query, string, optional) — Whether the worklog should be added to the issue even if the issue is not editable. For example, because the issue is closed.
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

Updates a worklog.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update any worklog or *Edit own worklogs* to update worklogs created by the user.
 *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
