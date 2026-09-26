---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-types
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/issuetype/{id}"
category: "Issue types"
writes_data: true
tool_note: "[[jira_delete_issue_type]]"
---
# Jira v3 - Delete issue type

**Delete issue type** — `DELETE /rest/api/3/issuetype/{id}`

- Run by the tool [[jira_delete_issue_type]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issuetype/{{param:id}}?alternativeIssueTypeId={{param:alternativeIssueTypeId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the issue type.
- `alternativeIssueTypeId` (query, string, optional) — The ID of the replacement issue type.

## Original description

Deletes the issue type. If the issue type is in use, all uses are updated with the alternative issue type (`alternativeIssueTypeId`). A list of alternative issue types are obtained from the [Get alternative issue types](#api-rest-api-3-issuetype-id-alternatives-get) resource.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
