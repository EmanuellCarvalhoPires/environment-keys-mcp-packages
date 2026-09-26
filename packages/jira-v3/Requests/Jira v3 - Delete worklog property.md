---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklog-properties
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}"
category: "Issue worklog properties"
writes_data: true
tool_note: "[[jira_delete_worklog_property]]"
---
# Jira v3 - Delete worklog property

**Delete worklog property** — `DELETE /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}`

- Run by the tool [[jira_delete_worklog_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/worklog/{{param:worklogId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `worklogId` (path, string, required) — The ID of the worklog.
- `propertyKey` (path, string, required) — The key of the property.

## Original description

Deletes a worklog property.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
