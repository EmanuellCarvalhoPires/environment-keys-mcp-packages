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
path: "/rest/api/3/worklog/deleted"
category: "Issue worklogs"
writes_data: false
tool_note: "[[jira_get_ids_of_deleted_worklogs]]"
---
# Jira v3 - Get IDs of deleted worklogs

**Get IDs of deleted worklogs** — `GET /rest/api/3/worklog/deleted`

- Run by the tool [[jira_get_ids_of_deleted_worklogs]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/worklog/deleted?since={{param:since}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `since` (query, string, optional) — The date and time, as a UNIX timestamp in milliseconds, after which deleted worklogs are returned.

## Original description

Returns a list of IDs and delete timestamps for worklogs deleted after a date and time.

This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of worklogs. The `lastPage` parameter is set to true on the last page of worklogs.

This resource does not return worklogs deleted during the minute preceding the request.

**[Permissions](#permissions) required:** Permission to access Jira.
