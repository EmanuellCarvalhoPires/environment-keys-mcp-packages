---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklogs
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/worklog/list"
category: "Issue worklogs"
writes_data: false
tool_note: "[[jira_get_worklogs]]"
---
# Jira v3 - Get worklogs

**Get worklogs** — `POST /rest/api/3/worklog/list`

- Run by the tool [[jira_get_worklogs]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/worklog/list?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `expand` (query, string, optional) — Use expand to include additional information about worklogs in the response. This parameter accepts properties that returns the properties of each worklog.
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

Returns worklog details for a list of worklog IDs.

The returned list of worklogs is limited to 1000 items.

**[Permissions](#permissions) required:** Permission to access Jira, however, worklogs are only returned where either of the following is true:

 *  the worklog is set as *Viewable by All Users*.
 *  the user is a member of a project role or group with permission to view the worklog.
