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
path: "/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member/{memberId}"
category: "Issue security schemes"
writes_data: true
tool_note: "[[jira_remove_member_from_issue_security_level]]"
---
# Jira v3 - Remove member from issue security level

**Remove member from issue security level** — `DELETE /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member/{memberId}`

- Run by the tool [[jira_remove_member_from_issue_security_level]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issuesecurityschemes/{{param:schemeId}}/level/{{param:levelId}}/member/{{param:memberId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `schemeId` (path, string, required) — The ID of the issue security scheme.
- `levelId` (path, string, required) — The ID of the issue security level.
- `memberId` (path, string, required) — The ID of the issue security level member to be removed.

## Original description

Removes an issue security level member from an issue security scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
