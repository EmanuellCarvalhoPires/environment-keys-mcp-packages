---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issuetypescheme/{issueTypeSchemeId}"
category: "Issue type schemes"
writes_data: true
tool_note: "[[jira_update_issue_type_scheme]]"
---
# Jira v3 - Update issue type scheme

**Update issue type scheme** — `PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}`

- Run by the tool [[jira_update_issue_type_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issuetypescheme/{{param:issueTypeSchemeId}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueTypeSchemeId` (path, string, required) — The ID of the issue type scheme.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "defaultIssueTypeId": "10002",
  "description": "A collection of issue types suited to use in a kanban style project.",
  "name": "Kanban Issue Type Scheme"
}
```

## Original description

Updates an issue type scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
