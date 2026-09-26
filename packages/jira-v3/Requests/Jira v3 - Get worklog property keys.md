---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklog-properties
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties"
category: "Issue worklog properties"
writes_data: false
tool_note: "[[jira_get_worklog_property_keys]]"
---
# Jira v3 - Get worklog property keys

**Get worklog property keys** — `GET /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties`

- Run by the tool [[jira_get_worklog_property_keys]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/worklog/{{param:worklogId}}/properties
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `worklogId` (path, string, required) — The ID of the worklog.

## Original description

Returns the keys of all properties for a worklog.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
