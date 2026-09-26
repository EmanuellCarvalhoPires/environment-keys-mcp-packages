---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId}"
category: "Issue type schemes"
writes_data: true
tool_note: "[[jira_remove_issue_type_from_issue_type_scheme]]"
---
# Jira v3 - Remove issue type from issue type scheme

**Remove issue type from issue type scheme** — `DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId}`

- Run by the tool [[jira_remove_issue_type_from_issue_type_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issuetypescheme/{{param:issueTypeSchemeId}}/issuetype/{{param:issueTypeId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `issueTypeSchemeId` (path, string, required) — The ID of the issue type scheme.
- `issueTypeId` (path, string, required) — The ID of the issue type.

## Original description

Removes an issue type from an issue type scheme.

This operation cannot remove:

 *  any issue type used by issues.
 *  any issue types from the default issue type scheme.
 *  the last standard issue type from an issue type scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
