---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issuesecurityschemes/{id}"
category: "Issue security schemes"
writes_data: false
tool_note: "[[jira_get_issue_security_scheme]]"
---
# Jira v3 - Get issue security scheme

**Get issue security scheme** — `GET /rest/api/3/issuesecurityschemes/{id}`

- Run by the tool [[jira_get_issue_security_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuesecurityschemes/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the issue security scheme. Use the Get issue security schemes operation to get a list of issue security scheme IDs.

## Original description

Returns an issue security scheme along with its security levels.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
 *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project that uses the requested issue security scheme.
