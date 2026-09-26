---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-screen-schemes
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}"
category: "Issue type screen schemes"
writes_data: true
tool_note: "[[jira_delete_issue_type_screen_scheme]]"
---
# Jira v3 - Delete issue type screen scheme

**Delete issue type screen scheme** — `DELETE /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}`

- Run by the tool [[jira_delete_issue_type_screen_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issuetypescreenscheme/{{param:issueTypeScreenSchemeId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `issueTypeScreenSchemeId` (path, string, required) — The ID of the issue type screen scheme.

## Original description

Deletes an issue type screen scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
