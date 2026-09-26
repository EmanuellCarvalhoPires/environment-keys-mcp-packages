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
path: "/rest/api/3/issuesecurityschemes/{schemeId}"
category: "Issue security schemes"
writes_data: true
tool_note: "[[jira_delete_issue_security_scheme]]"
---
# Jira v3 - Delete issue security scheme

**Delete issue security scheme** — `DELETE /rest/api/3/issuesecurityschemes/{schemeId}`

- Run by the tool [[jira_delete_issue_security_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issuesecurityschemes/{{param:schemeId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `schemeId` (path, string, required) — The ID of the issue security scheme.

## Original description

Deletes an issue security scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
