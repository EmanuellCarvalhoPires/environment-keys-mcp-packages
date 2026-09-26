---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklogs
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/{issueIdOrKey}/worklog/{id}"
category: "Issue worklogs"
writes_data: false
tool_note: "[[jira_get_worklog]]"
---
# Jira v3 - Get worklog

**Get worklog** — `GET /rest/api/3/issue/{issueIdOrKey}/worklog/{id}`

- Run by the tool [[jira_get_worklog]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/worklog/{{param:id}}?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `id` (path, string, required) — The ID of the worklog.
- `expand` (query, string, optional) — Use expand to include additional information about work logs in the response. This parameter accepts properties, which returns worklog properties.

## Original description

Returns a worklog.

Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
