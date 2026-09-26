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
path: "/rest/api/3/worklog/updated"
category: "Issue worklogs"
writes_data: false
tool_note: "[[jira_get_ids_of_updated_worklogs]]"
---
# Jira v3 - Get IDs of updated worklogs

**Get IDs of updated worklogs** — `GET /rest/api/3/worklog/updated`

- Run by the tool [[jira_get_ids_of_updated_worklogs]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/worklog/updated?since={{param:since}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `since` (query, string, optional) — The date and time, as a UNIX timestamp in milliseconds, after which updated worklogs are returned.
- `expand` (query, string, optional) — Use expand to include additional information about worklogs in the response. This parameter accepts properties that returns the properties of each worklog.

## Original description

Returns a list of IDs and update timestamps for worklogs updated after a date and time.

This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of worklogs. The `lastPage` parameter is set to true on the last page of worklogs.

This resource does not return worklogs updated during the minute preceding the request.

**[Permissions](#permissions) required:** Permission to access Jira, however, worklogs are only returned where either of the following is true:

 *  the worklog is set as *Viewable by All Users*.
 *  the user is a member of a project role or group with permission to view the worklog.
