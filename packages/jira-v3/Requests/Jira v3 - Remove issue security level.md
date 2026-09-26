---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}"
category: "Issue security schemes"
writes_data: true
tool_note: "[[jira_remove_issue_security_level]]"
---
# Jira v3 - Remove issue security level

**Remove issue security level** — `DELETE /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}`

- Run by the tool [[jira_remove_issue_security_level]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issuesecurityschemes/{{param:schemeId}}/level/{{param:levelId}}?replaceWith={{param:replaceWith}}
Authorization: {{service.auth_token}}
```

## Parameters

- `schemeId` (path, string, required) — The ID of the issue security scheme.
- `levelId` (path, string, required) — The ID of the issue security level to remove.
- `replaceWith` (query, string, optional) — The ID of the issue security level that will replace the currently selected level.

## Original description

Deletes an issue security level.

This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
