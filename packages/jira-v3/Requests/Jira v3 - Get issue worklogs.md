---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklogs
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/{issueIdOrKey}/worklog"
category: "Issue worklogs"
writes_data: false
tool_note: "[[jira_get_issue_worklogs]]"
---
# Jira v3 - Get issue worklogs

**Get issue worklogs** — `GET /rest/api/3/issue/{issueIdOrKey}/worklog`

- Run by the tool [[jira_get_issue_worklogs]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/worklog?startAt={{param:startAt}}&maxResults={{param:maxResults}}&startedAfter={{param:startedAfter}}&startedBefore={{param:startedBefore}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `startedAfter` (query, string, optional) — The worklog start date and time, as a UNIX timestamp in milliseconds, after which worklogs are returned.
- `startedBefore` (query, string, optional) — The worklog start date and time, as a UNIX timestamp in milliseconds, before which worklogs are returned.
- `expand` (query, string, optional) — Use expand to include additional information about worklogs in the response. This parameter acceptsproperties, which returns worklog properties.

## Original description

Returns worklogs for an issue (ordered by created time), starting from the oldest worklog or from the worklog started on or after a date and time.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Workloads are only returned where the user has:

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
