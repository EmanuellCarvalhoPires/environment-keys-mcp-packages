---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-level
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/securitylevel/{id}"
category: "Issue security level"
writes_data: false
tool_note: "[[jira_get_issue_security_level]]"
---
# Jira v3 - Get issue security level

**Get issue security level** — `GET /rest/api/3/securitylevel/{id}`

- Run by the tool [[jira_get_issue_security_level]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/securitylevel/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the issue security level.

## Original description

Returns details of an issue security level.

Use [Get issue security scheme](#api-rest-api-3-issuesecurityschemes-id-get) to obtain the IDs of issue security levels associated with the issue security scheme.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
