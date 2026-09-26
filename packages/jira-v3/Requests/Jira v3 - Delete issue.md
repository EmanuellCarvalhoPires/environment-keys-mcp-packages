---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/issue/{issueIdOrKey}"
category: "Issues"
writes_data: true
tool_note: "[[jira_delete_issue]]"
---
# Jira v3 - Delete issue

**Delete issue** — `DELETE /rest/api/3/issue/{issueIdOrKey}`

- Run by the tool [[jira_delete_issue]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}?deleteSubtasks={{param:deleteSubtasks}}
Authorization: {{service.auth_token}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `deleteSubtasks` (query, string, optional) — Whether the issue's subtasks are deleted when the issue is deleted.

## Original description

Deletes an issue.

An issue cannot be deleted if it has one or more subtasks. To delete an issue with subtasks, set `deleteSubtasks`. This causes the issue's subtasks to be deleted with the issue.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Delete issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
