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
path: "/rest/api/3/issuesecurityschemes/{id}"
category: "Issue security schemes"
writes_data: true
tool_note: "[[jira_update_issue_security_scheme]]"
---
# Jira v3 - Update issue security scheme

**Update issue security scheme** — `PUT /rest/api/3/issuesecurityschemes/{id}`

- Run by the tool [[jira_update_issue_security_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issuesecurityschemes/{{param:id}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the issue security scheme.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "My issue security scheme description",
  "name": "My issue security scheme name"
}
```

## Original description

Updates the issue security scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
