---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-worklog-properties
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}"
category: "Issue worklog properties"
writes_data: true
tool_note: "[[jira_set_worklog_property]]"
---
# Jira v3 - Set worklog property

**Set worklog property** — `PUT /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}`

- Run by the tool [[jira_set_worklog_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/worklog/{{param:worklogId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `worklogId` (path, string, required) — The ID of the worklog.
- `propertyKey` (path, string, required) — The key of the issue property. The maximum length is 255 characters.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Sets the value of a worklog property. Use this operation to store custom data against the worklog.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update any worklog or *Edit own worklogs* to update worklogs created by the user.
 *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
