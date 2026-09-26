---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-schemes
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issuetypescheme"
category: "Issue type schemes"
writes_data: true
tool_note: "[[jira_create_issue_type_scheme]]"
---
# Jira v3 - Create issue type scheme

**Create issue type scheme** — `POST /rest/api/3/issuetypescheme`

- Run by the tool [[jira_create_issue_type_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issuetypescheme
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "defaultIssueTypeId": "10002",
  "description": "A collection of issue types suited to use in a kanban style project.",
  "issueTypeIds": [
    "10001",
    "10002",
    "10003"
  ],
  "name": "Kanban Issue Type Scheme"
}
```

## Original description

Creates an issue type scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
