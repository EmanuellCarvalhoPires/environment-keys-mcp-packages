---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}"
category: "Issue security schemes"
writes_data: true
tool_note: "[[jira_update_issue_security_level]]"
---
# Jira v3 - Update issue security level

**Update issue security level** — `PUT /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}`

- Run by the tool [[jira_update_issue_security_level]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issuesecurityschemes/{{param:schemeId}}/level/{{param:levelId}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `schemeId` (path, string, required) — The ID of the issue security scheme level belongs to.
- `levelId` (path, string, required) — The ID of the issue security level to update.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "New level description",
  "name": "New level name"
}
```

## Original description

Updates the issue security level.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
