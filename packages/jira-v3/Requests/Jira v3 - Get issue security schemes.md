---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issuesecurityschemes"
category: "Issue security schemes"
writes_data: false
tool_note: "[[jira_get_issue_security_schemes]]"
---
# Jira v3 - Get issue security schemes

**Get issue security schemes** — `GET /rest/api/3/issuesecurityschemes`

- Run by the tool [[jira_get_issue_security_schemes]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuesecurityschemes
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns all [issue security schemes](https://confluence.atlassian.com/x/J4lKLg).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
