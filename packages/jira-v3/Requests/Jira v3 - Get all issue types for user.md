---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-types
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issuetype"
category: "Issue types"
writes_data: false
tool_note: "[[jira_get_all_issue_types_for_user]]"
---
# Jira v3 - Get all issue types for user

**Get all issue types for user** — `GET /rest/api/3/issuetype`

- Run by the tool [[jira_get_all_issue_types_for_user]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuetype
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns all issue types.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Issue types are only returned as follows:

 *  if the user has the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), all issue types are returned.
 *  if the user has the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, the issue types associated with the projects the user has permission to browse are returned.
 *  if the user is anonymous then they will be able to access projects with the *Browse projects* for anonymous users
 *  if the user authentication is incorrect they will fall back to anonymous
